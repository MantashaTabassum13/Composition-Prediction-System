import { AnimatePresence, motion } from "framer-motion";
import { useRouter } from "next/router";

import Layout from "../components/Layout";
import Transition from "../components/Transition";
import "../styles/globals.css";
import Body from "./body/Body";

function MyApp({ Component, pageProps }) {
  const router = useRouter();

  return (
   <>
   
         <AnimatePresence mode="wait">
        <motion.div key={router.route} className="h-full">
          <Transition />
          <Component {...pageProps} />
        </motion.div>
        
      </AnimatePresence>
   
   
    </>

  );
}

export default MyApp;
