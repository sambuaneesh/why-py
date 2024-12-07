import { promises as fs } from 'fs';
import { fileURLToPath } from 'url';
import { dirname, join } from 'path';

const __filename = fileURLToPath(import.meta.url);
const __dirname = dirname(__filename);

const files = [
    'lexer.py',
    'parser.py',
    'ast1.py',
    'eval.py',
    'environment.py',
    'object.py',
    'tok.py'
];

const sourceDir = join(__dirname, '..');
const targetDir = join(__dirname, 'public', 'interpreter');

// Create target directory if it doesn't exist
try {
    await fs.mkdir(targetDir, { recursive: true });
    console.log('Created target directory:', targetDir);
} catch (error) {
    if (error.code !== 'EEXIST') {
        console.error('Failed to create directory:', error);
    }
}

// Copy each file
for (const file of files) {
    const sourcePath = join(sourceDir, file);
    const targetPath = join(targetDir, file);
    
    try {
        await fs.copyFile(sourcePath, targetPath);
        console.log(`Copied ${file} to public/interpreter/`);
    } catch (error) {
        console.error(`Failed to copy ${file}:`, error.message);
    }
} 