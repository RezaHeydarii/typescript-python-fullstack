import { getStockBubbles, getStockList } from "@app/services/fetch/fund";
import React from "react";
import { StockBubbleChart } from "./components";

export default async function FundPage({
  params,
}: {
  params: { name: string };
}) {
  const data = await getStockBubbles(params.name);
  return (
    <main>
      <StockBubbleChart data={data} />
    </main>
  );
}

export async function generateStaticParams() {
  const stocks = await getStockList();
  return stocks.map((stock) => ({
    name: stock.name,
  }));
}
