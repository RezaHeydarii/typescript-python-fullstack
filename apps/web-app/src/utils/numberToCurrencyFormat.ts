export const numberToCurrencyFormat = (
  num: number,
  prefix: string = "Rial"
) => {
  return num
    .toFixed(2)
    .replace(/\d(?=(\d{3})+\.)/g, "$&,")
    .replace(".00", prefix);
};
