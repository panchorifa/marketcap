module.exports = {
  displayName: 'lint:eslint',
  runner: 'jest-runner-eslint',
  testMatch: [
    '<rootDir>/tests/**/*.js',
    '<rootDir>/src/**/*.js'
  ],
  testPathIgnorePatterns: [
  ]
};
