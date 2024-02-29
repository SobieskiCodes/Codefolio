// ./src/theme/theme.js

import { extendTheme } from '@chakra-ui/react';

const config = {
  initialColorMode: 'dark',
  useSystemColorMode: true,
};

const theme = extendTheme({
  config,
  styles: {
    global: {
      // Global styles are applied to the body element by default
      body: {
        // Set the background to black and then apply the SVG background image
        bg: 'black url(/theme/background.svg) no-repeat center center',
        bgSize: 'cover',
        color: 'white',
      },
      // ...
    },
  },
});

export default theme;
