import { defineConfig } from 'astro/config';
import starlight from '@astrojs/starlight';

// https://astro.build/config
export default defineConfig({
	integrations: [
		starlight({
			title: 'Custom Interpreter',
			description: 'Documentation for a simple yet powerful programming language interpreter written in Python',
			social: {
				github: 'https://github.com/stealthspectre/custom-interpreter',
			},
			sidebar: [
				{
					label: 'Getting Started',
					items: [
						{ label: 'Introduction', slug: 'getting-started/introduction' },
						{ label: 'Installation', slug: 'getting-started/installation' },
						{ label: 'Quick Start', slug: 'getting-started/quick-start' },
					],
				},
				{
					label: 'Language Guide',
					items: [
						{ label: 'Syntax Overview', slug: 'language-guide/syntax-overview' },
						{ label: 'Data Types', slug: 'language-guide/data-types' },
					],
				},
				{
					label: 'Implementation',
					items: [
						{ label: 'Lexer', slug: 'implementation/lexer' },
						{ label: 'Parser', slug: 'implementation/parser' },
						{ label: 'AST', slug: 'implementation/ast' },
					],
				},
			],
		}),
	],
});
