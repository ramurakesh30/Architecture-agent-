"use client";

import {
  useState
} from "react";

import {
  askReportQuestion
} from "@/src/app/services/chat";

interface Props {

  reportId: string;
}

interface Message {

  role:
    "user"
    |
    "assistant";

  content: string;
}

export default function
ChatAssistant({

  reportId

}: Props) {

  const [

    question,

    setQuestion

  ] = useState("");

  const [

    loading,

    setLoading

  ] = useState(
    false
  );

  const [

    messages,

    setMessages

  ] = useState<Message[]>([]);

  const suggestions = [

    "Why is my score low?",

    "What should I fix first?",

    "Explain the highest risk.",

    "How can I improve security?",

    "How can I improve compliance?"
  ];

  async function
  handleAsk() {

    if (
      !question.trim()
    ) {

      return;
    }

    const userMessage = {

      role:
        "user" as const,

      content:
        question

    };

    setMessages(

      previous => [

        ...previous,

        userMessage

      ]

    );

    const currentQuestion =
      question;

    setQuestion("");

    setLoading(
      true
    );

    try {

      const result =

        await askReportQuestion(

          reportId,

          currentQuestion

        );

      setMessages(

        previous => [

          ...previous,

          {

            role:
              "assistant",

            content:
              result.answer

          }

        ]

      );

    } catch (

      error

    ) {

      console.error(
        error
      );

      setMessages(

        previous => [

          ...previous,

          {

            role:
              "assistant",

            content:
              "Failed to get response from AI assistant."

          }

        ]

      );

    } finally {

      setLoading(
        false
      );
    }
  }

  return (

    <div
      className="
        bg-slate-900
        border
        border-slate-800
        rounded-lg
        p-6
        mt-8
      "
    >

      <h2
        className="
          text-2xl
          font-bold
          text-cyan-400
          mb-4
        "
      >
        AI Architecture Assistant
      </h2>

      <div
        className="
          flex
          flex-wrap
          gap-2
          mb-4
        "
      >

        {

          suggestions.map(

            (
              suggestion
            ) => (

              <button

                key={
                  suggestion
                }

                onClick={
                  () =>
                    setQuestion(
                      suggestion
                    )
                }

                className="
                  bg-slate-700
                  hover:bg-slate-600
                  text-sm
                  px-3
                  py-2
                  rounded-lg
                "
              >

                {
                  suggestion
                }

              </button>

            )

          )

        }

      </div>

      <div
        className="
          space-y-4
          max-h-96
          overflow-y-auto
          mb-4
        "
      >

        {

          messages.map(

            (
              message,
              index
            ) => (

              <div

                key={
                  index
                }

                className={

                  message.role ===
                  "user"

                  ?

                  `
                  bg-cyan-900/40
                  p-3
                  rounded-lg
                  ml-12
                  `

                  :

                  `
                  bg-slate-800
                  p-3
                  rounded-lg
                  mr-12
                  `
                }

              >

                <div
                  className="
                    text-xs
                    text-slate-400
                    mb-1
                  "
                >

                  {

                    message.role ===
                    "user"

                    ?

                    "You"

                    :

                    "Architecture AI"

                  }

                </div>

                <div>

                  {
                    message.content
                  }

                </div>

              </div>

            )

          )

        }

      </div>

      <div
        className="
          flex
          gap-2
        "
      >

        <input

          value={
            question
          }

          onChange={

            (
              e
            ) =>

            setQuestion(
              e.target.value
            )

          }

          onKeyDown={

            (
              e
            ) => {

              if (

                e.key ===
                "Enter"

              ) {

                handleAsk();
              }
            }

          }

          placeholder="
            Ask about this assessment...
          "

          className="
            flex-1
            bg-slate-800
            border
            border-slate-700
            rounded-lg
            px-4
            py-3
          "
        />

        <button

          onClick={
            handleAsk
          }

          disabled={
            loading
          }

          className="
            bg-cyan-600
            hover:bg-cyan-700
            disabled:bg-slate-700
            px-6
            py-3
            rounded-lg
            text-white
          "
        >

          {

            loading

            ?

            "Thinking..."

            :

            "Ask"

          }

        </button>

      </div>

    </div>

  );
}