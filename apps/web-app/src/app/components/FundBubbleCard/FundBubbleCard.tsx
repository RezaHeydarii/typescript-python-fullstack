import { numberToCurrencyFormat } from "@app/utils";
import { FundBubbleCardProps } from "./FundBubbleCard.type";
import moment from "moment-jalaali";
import Link from "next/link";

export const FundBubbleCard = (props: FundBubbleCardProps) => {
  const { bubbleData } = props;
  const { stock_name, last_price, date, nav_price } = bubbleData;
  return (
    <article className="px-2.5 pb-2.5 border border-gray-300 rounded-md">
      <div className="flex items-center justify-between w-full border-b border-b-gray-300 py-1.5 mb-2.5">
        <Link href={`/stock/${stock_name}`}>
          <h4 className="text-base font-bold hover:underline">{stock_name}</h4>
        </Link>
        <time className="text-xs text-gray-500">
          {moment(date).format("jYY/jMM/jDD-HH:mm")}
        </time>
      </div>
      <div className="flex space-x-5 items-center justify-between">
        <p className="text-sm">
          Last price:{" "}
          <strong>{numberToCurrencyFormat(last_price, "r")}</strong>
        </p>
        <p className="text-sm">
          Nav price: <strong>{numberToCurrencyFormat(nav_price, "r")}</strong>
        </p>
      </div>
    </article>
  );
};
