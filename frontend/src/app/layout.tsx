import Navbar from "@/src/components/ui/Navbar"
import "./globals.css";

export default function RootLayout({
  children,
}: {
  children: React.ReactNode;
}) {

  return (

    <html lang="en">

      <body
        className="
          min-h-screen
          bg-gradient-to-br
          from-slate-950
          via-slate-900
          to-slate-950
          text-white
        "
      >

        <Navbar />

        {children}

      </body>

    </html>
  );
}