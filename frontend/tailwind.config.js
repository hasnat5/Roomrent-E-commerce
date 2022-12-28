/** @type {import('tailwindcss').Config} */
module.exports = {
  content: ["./src/**/*.{js,jsx,ts,tsx}",],
  theme: {
    extend: {
      colors: {
        secondary: "#0D0F37",
        thirdy: "#555555", //gray
      },

      fontFamily: {
        signika: ['Signika', 'sans-serif'],
      },
    },
  },
  plugins: [require("daisyui")],

  daisyui: {
    themes: ["light"],
  },
}
