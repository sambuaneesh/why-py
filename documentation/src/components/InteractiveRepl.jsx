'use client';

import React, { useState, useEffect } from 'react';

// This is a limited version of WhyPy that only supports single-line input
// For multiline support and full functionality, please follow the Getting Started guide
// and clone the repository at: https://github.com/whypy/whypy

// Load Pyodide and the interpreter
async function initializePyodide() {
    // Load Pyodide
    const pyodide = await loadPyodide({
        indexURL: "https://cdn.jsdelivr.net/pyodide/v0.24.1/full/"
    });

    // Load the interpreter files in correct order
    const files = [
        'tok.py',
        'lexer.py',
        'parser.py',
        'ast1.py',
        'environment.py',
        'object.py',
        'eval.py'
    ];

    try {
        // Create a Python package for our interpreter
        const setupCode = `
import sys
import os

# Create a directory for our package
if not os.path.exists('/interpreter'):
    os.makedirs('/interpreter')
    
# Create an __init__.py to make it a package
with open('/interpreter/__init__.py', 'w') as f:
    f.write('')
`;
        await pyodide.runPythonAsync(setupCode);

        // Load each file and add it to our package
        for (const file of files) {
            const response = await fetch(`/interpreter/${file}`);
            if (!response.ok) {
                throw new Error(`Failed to load ${file}`);
            }
            const content = await response.text();
            
            // Fix imports in the content
            const fixedContent = content
                .replace(/from tok import/g, 'from interpreter.tok import')
                .replace(/from lexer import/g, 'from interpreter.lexer import')
                .replace(/from parser import/g, 'from interpreter.parser import')
                .replace(/from ast1 import/g, 'from interpreter.ast1 import')
                .replace(/from environment import/g, 'from interpreter.environment import')
                .replace(/from object import/g, 'from interpreter.object import')
                .replace(/from eval import/g, 'from interpreter.eval import');
            
            // Write the file to the virtual filesystem
            const writeCode = `
with open('/interpreter/${file}', 'w') as f:
    f.write(${JSON.stringify(fixedContent)})
`;
            await pyodide.runPythonAsync(writeCode);
        }

        // Initialize the environment and setup
        const initCode = `
import sys
sys.path.insert(0, '/')

from interpreter.tok import Token, TokenType
from interpreter.lexer import Lexer
from interpreter.parser import Parser
from interpreter.ast1 import *
from interpreter.environment import Environment
from interpreter.object import *
from interpreter.eval import Eval

env = Environment()

def print_parser_errors(errors):
    for msg in errors:
        print(f"└─ Arcane Error: {msg}")
`;
        await pyodide.runPythonAsync(initCode);

        return pyodide;
    } catch (error) {
        console.error('Error during initialization:', error);
        throw error;
    }
}

export default function InteractiveRepl() {
    if (typeof window === 'undefined') {
        return null;
    }

    const [input, setInput] = useState('');
    const [output, setOutput] = useState([
        { type: 'system', content: 'Welcome to the WhyPy REPL' },
        { type: 'system', content: 'Inscribe your incantations below. Use the sacred Enter to evaluate.' },
        { type: 'system', content: 'Note: This is a limited version that only supports single-line input.' },
        { type: 'system', content: 'For multiline support, please visit the Getting Started guide.' },
    ]);
    const [pyodide, setPyodide] = useState(null);
    const [isLoading, setIsLoading] = useState(true);

    useEffect(() => {
        let mounted = true;

        async function init() {
            try {
                const pyodideInstance = await initializePyodide();
                if (mounted) {
                    setPyodide(pyodideInstance);
                    setIsLoading(false);
                }
            } catch (error) {
                console.error('Failed to initialize Pyodide:', error);
                if (mounted) {
                    setOutput(prev => [...prev, 
                        { type: 'error', content: `Failed to initialize the interpreter: ${error.message}` }
                    ]);
                    setIsLoading(false);
                }
            }
        }

        init();

        return () => {
            mounted = false;
        };
    }, []);

    const executeCode = async () => {
        if (!input.trim()) return;

        setOutput(prev => [...prev, { type: 'input', content: input }]);

        try {
            const execCode = `
import io
import sys

stdout = io.StringIO()
sys.stdout = stdout

try:
    lexer = Lexer(${JSON.stringify(input)})
    parser = Parser(lexer)
    program = parser.parse_program()
    
    if len(parser.errors) != 0:
        print_parser_errors(parser.errors)
    else:
        evaluated = Eval(program, env)
        if evaluated is not None:
            print(f"└─ The runes speak: {evaluated.inspect()}")
except Exception as e:
    print(f"└─ Arcane Error: {str(e)}")

output = stdout.getvalue().strip()
sys.stdout = sys.__stdout__
output
`;
            const result = await pyodide.runPythonAsync(execCode);
            if (result) {
                setOutput(prev => [...prev, 
                    { type: result.includes('Arcane Error') ? 'error' : 'output', 
                      content: result }
                ]);
            }
        } catch (error) {
            console.error('Execution error:', error);
            setOutput(prev => [...prev, 
                { type: 'error', content: `└─ Arcane Error: ${error.message}` }
            ]);
        }
        
        setInput('');
    };

    const handleKeyDown = (e) => {
        if (e.key === 'Enter' && !e.shiftKey) {
            e.preventDefault();
            executeCode();
        }
    };

    if (isLoading) {
        return (
            <div style={{
                border: '1px solid #2f3447',
                borderRadius: '8px',
                padding: '2rem',
                textAlign: 'center',
                color: '#7957d5',
                backgroundColor: '#1a1b26',
                fontFamily: 'monospace'
            }}>
                Summoning the mystical interpreter...
            </div>
        );
    }

    return (
        <div style={{
            border: '1px solid #2f3447',
            borderRadius: '8px',
            overflow: 'hidden',
            margin: '1rem 0',
            backgroundColor: '#1a1b26',
            fontFamily: 'monospace'
        }}>
            <div style={{
                backgroundColor: '#7957d5',
                padding: '0.5rem 1rem',
                display: 'flex',
                justifyContent: 'space-between',
                alignItems: 'center'
            }}>
                <span style={{ color: 'white', fontSize: '0.9em', fontWeight: 'bold' }}>
                    WHYPY INTERACTIVE REPL
                </span>
                <div style={{ fontSize: '0.8em', color: 'white' }}>
                    PRESS ENTER TO EVALUATE
                </div>
            </div>

            <div style={{
                backgroundColor: '#1a1b26',
                color: '#a9b1d6',
                padding: '1rem',
                minHeight: '200px',
                maxHeight: '400px',
                overflowY: 'auto',
                whiteSpace: 'pre-wrap',
                fontSize: '0.9em'
            }}>
                {output.map((item, index) => (
                    <div key={index} style={{
                        color: item.type === 'system' ? '#7957d5' : 
                              item.type === 'input' ? '#a9b1d6' : 
                              item.type === 'error' ? '#ff5555' : '#50fa7b',
                        marginBottom: '0.25rem'
                    }}>
                        {item.type === 'input' && (
                            <>
                                <div style={{ color: '#7957d5' }}>┌──(Mystic User⚡Browser)-[Grimoire]</div>
                                <span style={{ color: '#ff79c6' }}>└─⚡ </span>
                            </>
                        )}
                        {item.content}
                    </div>
                ))}
            </div>

            <div style={{
                borderTop: '1px solid #2f3447',
                padding: '0.5rem',
                backgroundColor: '#1a1b26'
            }}>
                <input
                    value={input}
                    onChange={(e) => setInput(e.target.value)}
                    onKeyDown={handleKeyDown}
                    placeholder="Enter WhyPY code here..."
                    style={{
                        width: '100%',
                        padding: '0.5rem',
                        backgroundColor: '#24283b',
                        color: '#a9b1d6',
                        border: '1px solid #2f3447',
                        borderRadius: '4px',
                        fontFamily: 'inherit',
                        outline: 'none'
                    }}
                />
            </div>
        </div>
    );
} 