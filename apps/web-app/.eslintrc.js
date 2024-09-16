/** @type {import("eslint").Linter.Config} */
export default {
  root: true,
  extends: ["@fin-tools/eslint-config/next.js"],
  parser: "@typescript-eslint/parser",
  parserOptions: {
    project: true,
  },
};
