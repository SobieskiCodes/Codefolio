// ./src/theme/theme.js

import { extendTheme } from '@chakra-ui/react';

const config = {
  initialColorMode: 'dark',
  useSystemColorMode: true, // Set this to true to use the system color mode
};

const theme = extendTheme({ config });

export default theme;
