/** @type {import('tailwindcss').Config} */
module.exports = {
    darkMode: "class",
    content: ["./index.html", "./src/**/*.{vue,js,ts,jsx,tsx}"],
    theme: {
        extend: {
            colors: {
                primary: {
                    "light-60": "#b8dfb9",
                    "light-40": "#94cf97",
                    "light-20": "#71bf74",
                    DEFAULT: "#4DAF51",
                    "dark-20": "#3e8c41",
                    "dark-40": "#2e6931",
                    "dark-60": "#1f4620",
                },
            },
        },
    },
    plugins: [],
};
