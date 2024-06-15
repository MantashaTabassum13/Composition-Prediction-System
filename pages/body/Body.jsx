import React, { useEffect, useState } from 'react';

function Body() {
  const [isScrollable, setIsScrollable] = useState(false);

  useEffect(() => {
    const handleResize = () => {
      const windowHeight = window.innerHeight;
      const iframe = document.querySelector('iframe');
      const iframeHeight = iframe.offsetHeight;
      setIsScrollable(iframeHeight >= windowHeight * 2.7);
      if (!isScrollable) {
        iframe.contentWindow.scrollTo(0, 0);
      }
    };

    window.addEventListener('resize', handleResize);
    handleResize();

    return () => {
      window.removeEventListener('resize', handleResize);
    };
  }, [isScrollable]);

  return (
    <iframe
      src="/abc.html"
      className="w-screen"
      style={{
        height: '100vh',
        overflowY: isScrollable ? 'auto' : 'hidden',
        scrollbarWidth: 'none',
        '-ms-overflow-style': 'none',
        '-webkit-scrollbar': {
          display: 'none',
        },
      }}
    />
  );
}

export default Body;
