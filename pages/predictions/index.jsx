import { motion } from "framer-motion";
import { useRouter } from "next/router";
import { useState, useEffect } from "react";
import Bulb from "../../components/Bulb";
import Circles from "../../components/Circles";
import ServiceSlider from "../../components/ServiceSlider";
import { fadeIn } from "../../variants";
import Layout from "../../components/Layout";

const Index = () => {
  const router = useRouter();
  const [predictions, setPredictions] = useState(null);

  // Fetch predictions data when component mounts
  useEffect(() => {
    // Retrieve predictions from query parameters
    const { Team_Leader, Avenger1, Avenger2, Avenger3 } = router.query;
    if (Team_Leader && Avenger1 && Avenger2 && Avenger3) {
      // Set predictions state
      setPredictions({ Team_Leader, Avenger1, Avenger2, Avenger3 });
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
                Team Composition <span className="text-accent">.</span>
              </motion.h2>
              <motion.p
                variants={fadeIn("up", 0.4)}
                initial="hidden"
                animate="show"
                exit="hidden"
                className="mb-4 max-w-[400px] mx-auto lg:mx-0"
              >
               <div className="">
              
              {predictions && (
                
                  <>
                  <p style={{color:"white",fontSize:"Larger"}}>Team Leader: {predictions.Team_Leader}</p>
                  <p style={{color:"white",fontSize:"Larger"}}>Avenger 1: {predictions.Avenger1}</p>
                  <p style={{color:"white",fontSize:"Larger"}}>Avenger 2: {predictions.Avenger2}</p>
                  <p style={{color:"white",fontSize:"Larger"}}>Avenger 3: {predictions.Avenger3}</p>
                  </>
              )}
            </div>
              </motion.p>

            </div>
            {/* <div className="login">
              <h1 className="login__title">Predictions</h1>
              {predictions && (
                <div className="login__form">
                  <h2 className="login__title">PREDICTIONS</h2>
                  <p>Team Leader: {predictions.Team_Leader}</p>
                  <p>Avenger1: {predictions.Avenger1}</p>
                  <p>Avenger2: {predictions.Avenger2}</p>
                  <p>Avenger3: {predictions.Avenger3}</p>
                </div>
              )}
            </div> */}
            {/* slider */}
            {/* <motion.div
              variants={fadeIn("down", 0.6)}
              initial="hidden"
              animate="show"
              exit="hidden"
              className="w-full xl:max-w-[65%]"
            >
              <ServiceSlider />
            </motion.div> */}
          </div>
        </div>
        <Bulb />
      </div>
    </Layout>
  );
};

export default Index;
