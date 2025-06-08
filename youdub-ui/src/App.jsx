import DubForm from "./components/DubForm";
import { motion } from "framer-motion";

export default function App() {
  return (
    <div className="min-h-screen bg-gradient-to-b from-[#0f0c29] via-[#302b63] to-[#24243e] text-white flex flex-col items-center px-4">
      <motion.h1
        initial={{ opacity: 0, y: -20 }}
        animate={{ opacity: 1, y: 0 }}
        transition={{ duration: 0.8 }}
        className="text-4xl md:text-5xl font-bold mt-16 text-center"
      >
        🌐 YouDub – Understand Any YouTube Video in Your Language
      </motion.h1>

      <DubForm />
    </div>
  );
}

