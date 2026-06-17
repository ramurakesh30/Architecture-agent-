"use client";

import {

  useEffect,

  useState

} from "react";

import { useRouter }
from "next/navigation";

import {

  getTrendData

} from "@/src/app/services/history";

import TrendChart
from "@/src/components/ui/TrendChart";

export default function
TrendsPage() {
  
  const router =
    useRouter();

  useEffect(() => {

    const token =

      localStorage.getItem(
        "token"
      );

    if (!token) {

      router.push(
        "/login"
      );
    }

  }, []);

  const [

    trendData,

    setTrendData

  ] = useState<any[]>([]);

  useEffect(() => {

    getTrendData()

      .then(

        (
          data
        ) => {

          console.log(
            data
          );

          setTrendData(
            data
          );
        }
      );

  }, []);

  return (

    <main
      className="
        max-w-6xl
        mx-auto
        p-8
      "
    >

      <h1
        className="
          text-4xl
          font-bold
          mb-8
        "
      >
        Trend Analysis
      </h1>

      <TrendChart

        data={
          trendData
        }

      />

    </main>
  );
}