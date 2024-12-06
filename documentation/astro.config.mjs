import { defineConfig } from 'astro/config';
import starlight from '@astrojs/starlight';

// https://astro.build/config
export default defineConfig({
	integrations: [
		starlight({
			title: 'WhyPy',
			description: 'A programming language that questions its own existence. Why? We don\'t know either.',
			customCss: [
				'./src/styles/custom.css',
			],
			social: {
				github: 'https://github.com/sambuaneesh/why-py',
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
						{ label: 'Esoteric Semantics', slug: 'language-guide/esoteric-semantics' },
					],
				},
				{
					label: 'Implementation',
					items: [
						{ label: 'Lexer', slug: 'implementation/lexer' },
						{ label: 'Parser', slug: 'implementation/parser' },
						{ label: 'AST', slug: 'implementation/ast' },
						{ label: 'Interpreter', slug: 'implementation/interpreter' },
					],
				},
				{
					label: 'Examples',
					items: [
						{ label: 'Basic Examples', slug: 'examples/basic' },
						{ label: 'Advanced Examples', slug: 'examples/advanced' },
						{ label: 'Design Patterns', slug: 'examples/patterns' },
					],
				},
			],
			head: [
				{
					tag: 'link',
					attrs: {
						rel: 'icon',
						href: '/favicon.svg',
						type: 'image/svg+xml',
					},
				},
				{
					tag: 'link',
					attrs: {
						rel: 'stylesheet',
						href: 'https://fonts.googleapis.com/css2?family=Cinzel:wght@400;500;600;700&family=Fira+Code:wght@400;500&display=swap',
					},
				},
			],
			customCss: [
				'./src/styles/custom.css',
			],
		}),
	],
});
