"use client";
import React, { useMemo } from "react";
import { BubblesBarChartProps } from "./BubblesBarChart.type";
import {
  Bar,
  CartesianGrid,
  Cell,
  ComposedChart,
  Legend,
  ResponsiveContainer,
  Tooltip,
  XAxis,
  YAxis,
} from "recharts";
import cls from "classnames";
import { useRouter } from "next/navigation";

export const BubblesBarChart = (props: BubblesBarChartProps) => {
  const { data } = props;
  const router = useRouter();
  const chartData = useMemo(
    () =>
      data.map((d) => ({
        name: d.stock_name,
        bubble: (((d.last_price - d.nav_price) / d.nav_price) * 100),
      })),
    [data]
  );
  return (
    <div className="w-full h-[500px]">
      <ResponsiveContainer width="100%" height="100%">
        <ComposedChart
          data={chartData}
          layout="vertical"
          width={400}
          height={500}
          margin={{ top: 50, left: 50, right: 50 }}
        >
          <CartesianGrid stroke="#f5f5f5" />
          <XAxis type="number" />
          <YAxis
            type="category"
            dataKey="name"
            scale="auto"
            fontSize="0.9rem"
          />
          <Tooltip />
          <Legend />
          <Bar dataKey="bubble" barSize={20}>
            {chartData.map((d) => {
              return (
                <Cell
                  key={d.name}
                  onClick={() => router.push(`/stock/${d.name}`)}
                  className={cls({
                    "fill-error": d.bubble > 5,
                    "fill-warning": d.bubble >= 3 && d.bubble <= 5,
                    "fill-green-1": d.bubble < 3,
                  })}
                />
              );
            })}
          </Bar>
        </ComposedChart>
      </ResponsiveContainer>
    </div>
  );
};
