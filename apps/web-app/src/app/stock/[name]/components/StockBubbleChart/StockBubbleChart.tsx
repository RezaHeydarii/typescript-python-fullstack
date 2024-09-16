"use client";

import React, { useMemo } from "react";
import { StockBubbleChartProps } from "./StockBubbleChart.type";
import {
  Bar,
  CartesianGrid,
  ComposedChart,
  Line,
  ResponsiveContainer,
  Tooltip,
  XAxis,
  YAxis,
} from "recharts";
import moment from "moment-jalaali";

export const StockBubbleChart = (props: StockBubbleChartProps) => {
  const { data } = props;
  const chartData = useMemo(() => {
    let bubbleSum = 0;
    return data.map((d, index) => {
      const bubble = ((d.last_price - d.nav_price) / d.nav_price) * 100;
      bubbleSum += bubble;
      return {
        date: moment(d.date).format("jYY/jMM/jDD-HH:mm"),
        bubble,
        simpleMean: bubbleSum / (index + 1),
      };
    });
  }, [data]);
  const chartDataWithMean = useMemo(() => {
    const m = chartData.reduce((mean, d, index) => {
      if (index === data.length - 1) {
        return (mean + d.bubble) / data.length;
      }
      return mean + d.bubble;
    }, 0);
    return chartData.map((d) => ({ ...d, mean: m }));
  }, [chartData]);
  return (
    <div className="w-full h-[500px]">
      <ResponsiveContainer width="100%" height="100%">
        <ComposedChart
          width={500}
          height={400}
          data={chartDataWithMean}
          margin={{
            top: 20,
            right: 20,
            bottom: 20,
            left: 20,
          }}
        >
          <CartesianGrid stroke="#f5f5f5" />
          <Tooltip />
          <XAxis dataKey="date" fontSize=".8rem" />
          <YAxis />
          <Bar dataKey="bubble" barSize={10} className="fill-primary" />
          <Line dataKey="simpleMean" className="!stroke-warning" />
          <Line dataKey="mean" className="!stroke-error" />
        </ComposedChart>
      </ResponsiveContainer>
    </div>
  );
};
