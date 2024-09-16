export const appFetch: typeof fetch = (url, ...rest) => {
  const newUrl = process.env.API_BASE_URL
    ? process.env.API_BASE_URL + url
    : url;
  return fetch(newUrl, ...rest);
};
