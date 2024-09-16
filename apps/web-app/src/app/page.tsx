import { getStockBubbles } from "@app/services/fetch/fund";
import { BubblesBarChart, FundBubbleCard } from "./components";

export default async function Home() {
  const data = await getStockBubbles();

  return (
    <main className="px-10 pt-5">
      <h1 className="text-lg font-bold mb-2.5">Latest fund data:</h1>
      <section className="grid grid-cols-1 sm:grid-cols-2 md:grid-cols-3 lg:grid-cols-4 xl:grid-cols-5 gap-2">
        {data.map((bubble) => {
          return <FundBubbleCard key={bubble.id} bubbleData={bubble} />;
        })}
      </section>
      <h1 className="text-lg font-bold mb-2.5 mt-10">Latest bubble list:</h1>
      <section className="bg-white border border-gray-300 rounded-lg pb-6">
        <BubblesBarChart data={data} />
      </section>
    </main>
  );
}
