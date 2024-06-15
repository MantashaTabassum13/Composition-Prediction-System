import Link from "next/link";
import { usePathname } from "next/navigation";

// nav data
export const navData = [
  { name: "Natasha", path: "/", icon: "/n1.png" },
  { name: "Iron Man", path: "/about", icon: "/i1.png" },
  { name: "Thor", path: "/services", icon: "/t1.png" },
  { name: "Hawkeye", path: "/work", icon: "h1.png" },
  { name: "Black Panther", path: "/testimonials", icon: "/b1.png" },
  { name: "Captain America", path: "/contact", icon: "/c1.png" },
];

const Nav = () => {
  const pathname = usePathname();

  return (
    <nav className="flex flex-col items-center xl:justify-center gap-y-4 fixed h-max bottom-0 mt-auto xl:right-[2%] z-50 top-0 w-full xl:w-16 xl:max-w-md xl:h-screen">
      <div className="flex w-full xl:flex-col items-center justify-between xl:justify-center gap-y-10 px-4 md:px-40 xl:px-0 h-[80px] xl:h-max py-8 bg-white/10 backdrop-blur-sm text-3xl xl:text-xl xl:rounded-full">
        {navData.map((link, i) => (
          <Link
            className={`${
              link.path === pathname && "text-accent"
            } relative flex items-center group hover:text-accent transition-all duration-300`}
            href={link.path}
            key={i}
          >
            {/* tolltip */}
            <div
              role="tooltip"
              className="absolute pr-14 right-0 hidden xl:group-hover:flex"
            >
              <div className="bg-white relative flex text-primary items-center p-[6px] rounded-[3px]">
                <div className="text-[12px] leading-none font-semibold capitalize">
                  {link.name}
                </div>

                {/* triangle */}
                <div
                  className="border-solid border-l-white border-l-8 border-y-transparent border-y-[6px] border-r-0 absolute -right-2"
                  aria-hidden
                />
              </div>
            </div>

            {/* icon */}
            <div>
              <img
                src={link.icon}
                alt={link.name}
                style={{ height: "35px" }} // Set custom height
              />
            </div>
          </Link>
        ))}
      </div>
    </nav>
  );
};

export default Nav;
