"use client";

import {

  ResponsiveContainer,

  LineChart,

  Line,

  XAxis,

  YAxis,

  Tooltip,

  CartesianGrid

} from "recharts";

interface TrendPoint {

  date: string;

  score: number;
}

interface TrendChartProps {

  data: TrendPoint[];
}

export default function TrendChart({

  data

}: TrendChartProps) {

  return (

    <div
      className="
        bg-slate-900
        border
        border-slate-800
        rounded-lg
        p-6
      "
    >

      <h2
        className="
          text-2xl
          font-bold
          mb-6
        "
      >
        Overall Score Trend
      </h2>

      <div
        className="
          h-96
        "
      >

        <ResponsiveContainer
          width="100%"
          height="100%"
        >

          <LineChart
            data={data}
          >

            <CartesianGrid />

            <XAxis
              dataKey="date"
            />

            <YAxis />

            <Tooltip />

            <Line
              type="monotone"
              dataKey="score"
            />

          </LineChart>

        </ResponsiveContainer>

      </div>

    </div>

  );
}