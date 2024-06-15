import { Sora } from "next/font/google";
import Head from "next/head";

import Header from "../components/Header";
import Nav from "../components/Nav";
import TopLeftImg from "../components/TopLeftImg";

// setup font
const sora = Sora({
  subsets: ["latin"],
  variable: "--font-sora",
  weight: ["100", "200", "300", "400", "500", "600", "700", "800"],
});

const Layout = ({ children }) => {
  return (
    <main
      className={`page bg-site text-white bg-cover bg-no-repeat ${sora.variable} font-sora relative`}
    >
      {/* metadata */}
      <Head>
        <title>Avenger Assemble</title>

    <script src="https://dmitrinaumov.github.io/Paralax-effect-with-gsap-scrolltrigger/js/splitting.min.js"></script>
<script src="https://dmitrinaumov.github.io/Paralax-effect-with-gsap-scrolltrigger/js/luxy.js"></script>
<script src="https://unpkg.co/gsap@3/dist/gsap.min.js"></script>
<script src="https://unpkg.com/gsap@3/dist/ScrollTrigger.min.js"></script>
  <script src="https://cdpn.io/cpe/boomboom/pen.js?key=pen.js-6d27079a-db63-0d9f-e776-eadb084dbf03" crossorigin=""></script>

      
      </Head>

      <TopLeftImg />
      <Nav />
      {/* <Header /> */}

      {/* main content */}
      {children}
    </main>
  );
};

export default Layout;
