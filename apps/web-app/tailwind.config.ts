import type { Config } from "tailwindcss";

const config: Config = {
  content: [
    "./src/pages/**/*.{js,ts,jsx,tsx,mdx}",
    "./src/components/**/*.{js,ts,jsx,tsx,mdx}",
    "./src/app/**/*.{js,ts,jsx,tsx,mdx}",
  ],
  theme: {
    extend: {
      colors: {
        primary: "#35155D",
        secondary: "#35155D",
        trinary: "#4477CE",
        info: "#8CABFF",
        green: {
          1: "#03C988",
        },
        warning: "#E3651D",
        error: "#750E21",
      },
      boxShadow:{
        card:" 1px 1px 5px 3px rgba(0,0,0,0.30);"
      }
    },
  },
  plugins: [],
};
export default config;
