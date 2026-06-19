"use client";

import {
  useEffect,
  useRef
} from "react";

interface Props {

  diagram: string;
}

export default function MermaidRenderer({

  diagram

}: Props) {

  const containerRef =
    useRef<HTMLDivElement>(
      null
    );

  useEffect(() => {

    async function render() {

      if (
        !diagram
      ) {
        return;
      }

      const mermaid =
        (
          await import(
            "mermaid"
          )
        ).default;

      mermaid.initialize({

        startOnLoad:
          false

      });

      const cleanedDiagram =

        diagram

          .replace(
            /```mermaid/g,
            ""
          )

          .replace(
            /```/g,
            ""
          )

          .trim();

      const result =

        await mermaid.render(

          `mermaid-${Date.now()}`,

          cleanedDiagram

        );

      if (
        containerRef.current
      ) {

        containerRef.current.innerHTML =
          result.svg;
      }
    }

    render();

  }, [diagram]);

  return (

    <div

      ref={
        containerRef
      }

      className="
        bg-white
        rounded-lg
        p-4
        overflow-auto
      "

    />

  );
}