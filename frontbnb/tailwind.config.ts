import type { Config } from "tailwindcss";

export default {
  content: [
    "./src/pages/**/*.{js,ts,jsx,tsx,mdx}",
    "./src/components/**/*.{js,ts,jsx,tsx,mdx}",
    "./src/app/**/*.{js,ts,jsx,tsx,mdx}",
  ],
  theme: {
    extend: {
      // personnaliser le css
      colors: {
        'airbnb': '#ff385c',
        'airbnb-dark': '#d50027'
      },
    },
  },
  plugins: [],
} satisfies Config;
