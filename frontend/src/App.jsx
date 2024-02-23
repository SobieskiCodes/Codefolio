import React from 'react';
import { ChakraProvider, Box, Tab, TabList, Tabs, TabPanels, TabPanel, Flex } from "@chakra-ui/react";
import theme from './theme/theme'; 
import './App.css';
import ViewOne from './pages/ViewOne';
import StoreView from './pages/StoreView';
import ViewThree from './pages/ViewThree';
import GuessingGame from './pages/GuessingGame/GuessingGame';
import ColorModeToggle from './components/ColorModeToggle'; // Import the color mode toggle component

// We will be automating this with file/project names, from a folder we will traverse.
// githubs "raw" comes back as json - so we could have a static "name" variable to parse

const tabData = [
  { name: 'Tab 1', component: ViewOne },
  { name: 'Tab 2', component: StoreView },
  { name: 'Tab 3', component: ViewThree },
  { name: 'Tab 4', component: GuessingGame }
];

function App() {
  return (
    <ChakraProvider theme={theme}>
      <Flex direction="column" h="100vh">
        <Flex justify="space-between" align="center" p={4} w="100%">
          <Box>Title</Box>
          <ColorModeToggle /> 
        </Flex>
        <Tabs isFitted variant="enclosed" w="100%">
          <TabList>
            {tabData.map(tab => <Tab key={tab.name}>{tab.name}</Tab>)}
          </TabList>
          <TabPanels>
            {tabData.map(tab => (
              <TabPanel key={tab.name}>
                <Box borderWidth="2px" borderRadius="lg" p={4} shadow="sm" h="100%">
                  {React.createElement(tab.component)}
                </Box>
              </TabPanel>
            ))}
          </TabPanels>
        </Tabs>
      </Flex>
    </ChakraProvider>
  );
}

export default App;
