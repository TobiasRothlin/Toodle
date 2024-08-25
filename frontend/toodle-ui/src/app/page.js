import Image from "next/image";
import EventView from "./eventView";
import NewEvent from "./newEvent";

export default function Home() {
  return (
    <main className="flex min-h-screen flex-col items-center  p-24">
      <h1 className="text-4xl font-bold p-5">Welcome to Toodle</h1>
      <div className="grid grid-cols-2 gap-4">
        <NewEvent></NewEvent>
        <EventView></EventView>
      </div>
      
    </main>
  );
}
