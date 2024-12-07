# WhyPY Documentation

This is the documentation site for WhyPY, built with [Astro](https://astro.build) and [Starlight](https://starlight.astro.build).

## Features

- 📚 Comprehensive documentation for WhyPY
- 🔄 Interactive REPL in the browser
- 🎨 Custom mystical theme
- 📱 Responsive design
- 🚀 Fast and SEO-friendly

## Development

### Prerequisites

- Node.js 16 or higher
- Bun (recommended) or npm

### Setup

1. Clone the repository:
bash
git clone https://github.com/yourusername/whypy.git
cd whypy/documentation
```

2. Install dependencies:
```bash
bun install
# or
npm install
```

3. Start the development server:
```bash
bun run dev
# or
npm run dev
```

The site will be available at `http://localhost:4321`.

### Project Structure

```
documentation/
├── public/              # Static assets
│   ├── favicon.svg
│   └── interpreter/     # WhyPY interpreter files
├── src/
│   ├── assets/         # Site assets
│   ├── components/     # React components
│   ├── content/        # Documentation content
│   └── styles/         # Custom CSS
├── astro.config.mjs    # Astro configuration
└── package.json        # Project dependencies
```

### Building

To build the site for production:

```bash
bun run build
# or
npm run build
```

The built site will be in the `dist` directory.

## Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License - see the LICENSE file for details.
```