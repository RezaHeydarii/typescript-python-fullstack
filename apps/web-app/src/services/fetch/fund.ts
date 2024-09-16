import { FundBubbleData, StockType } from "@app/types";
import { appFetch } from "./appFetch";

export const getStockList = async () => {
  const stockList = await appFetch(`/stock`, {
    next: { revalidate: 1000 },
  });

  return stockList.json() as Promise<StockType[]>;
};

export const getStockBubbles = async (stockName?: string) => {
  const list = await appFetch(`/bubbles/${stockName || "latest"}`, {
    next: { revalidate: 1000 },
  });

  return list.json() as Promise<FundBubbleData[]>;
};
