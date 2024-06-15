import { motion } from "framer-motion";
import { useRouter } from "next/router";
import { useState, useEffect } from "react";
import Bulb from "../../components/Bulb";
import Circles from "../../components/Circles";
import ServiceSlider from "../../components/ServiceSlider";
import { fadeIn } from "../../variants";
import Layout from "../../components/Layout";

const index = () => {
  const router = useRouter();
  const [dangerPercent, setDangerPercent] = useState(null);

  // Fetch danger percent data when component mounts or query parameters change
  useEffect(() => {
    // Retrieve danger percent from query parameters
    const { danger_percent } = router.query;
    if (danger_percent) {
      // Set danger percent state
      setDangerPercent(danger_percent);
    }
  }, [router.query]);

  return (
    <Layout>
      <div className="h-full bg-primary/30 py-36 flex items-center">
        <Circles />
        <div className="container mx-auto">
          <div className="flex flex-col xl:flex-row gap-x-8">
            {/* text */}
            <div className="text-center flex xl:w-[30vw] flex-col lg:text-left mb-4 xl:mb-0">
              <motion.h2
                variants={fadeIn("up", 0.2)}
                initial="hidden"
                animate="show"
                exit="hidden"
                className="h2 xl:mt-8"
              >
                Danger Probability <span className="text-accent">.</span>
              </motion.h2>
              <motion.p
                variants={fadeIn("up", 0.4)}
                initial="hidden"
                animate="show"
                exit="hidden"
                className="mb-4 max-w-[400px] mx-auto lg:mx-0"
              >
                <div className="">
                  {dangerPercent && (
                    <>
                      <p style={{ color: "white", fontSize: "larger" }}>
                        Danger Percent: {dangerPercent}
                      </p>
                    </>
                  )}
                </div>
              </motion.p>
              <div>
                <img src="/paris.jpg" alt="" srcset="" />
              </div>
            </div>
          </div>
        </div>
        <Bulb />
      </div>
    </Layout>
  );
};

export default index;
