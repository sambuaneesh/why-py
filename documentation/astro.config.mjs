import { defineConfig } from 'astro/config';
import starlight from '@astrojs/starlight';
import react from '@astrojs/react';

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
					autogenerate: { directory: 'getting-started' }
				},
				{
					label: 'Language Guide',
					autogenerate: { directory: 'language-guide' }
				},
				{
					label: 'Implementation',
					autogenerate: { directory: 'implementation' }
				},
				{
					label: 'Examples',
					autogenerate: { directory: 'examples' }
				}
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
				{
					tag: 'script',
					attrs: {
						src: 'https://cdn.jsdelivr.net/pyodide/v0.24.1/full/pyodide.js',
					},
				},
			],
		}),
		react(),
	],
});
