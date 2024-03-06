import React, { useState, Suspense } from 'react';
import { ChakraProvider, Box, Tab, TabList, Tabs, TabPanels, TabPanel, Flex, Spinner } from '@chakra-ui/react';
import theme from './theme/theme';
import './App.css';
import ColorModeToggle from './components/ColorModeToggle';
import { WebSocketProvider } from './components/websocket/WebSocketProvider';

const tabData = [
  { name: 'Fishbone', component: React.lazy(() => import('./pages/CPS120/fishbone/FishboneAquatics')) },
  { name: 'Store View', component: React.lazy(() => import('./pages/CPS120/StoreView')) },
  { name: 'Guessing Game', component: React.lazy(() => import('./pages/CPS120/GuessingGame/GuessingGame')) },
  { name: 'WebSocket', component: React.lazy(() => import('./pages/websocket')) },
];

function App() {
  const [tabIndex, setTabIndex] = useState(0);

  const handleTabsChange = (index) => {
    setTabIndex(index);
  };

  return (
    <ChakraProvider theme={theme}>
      <WebSocketProvider>
      <Flex direction="column" h="100vh">
        <Flex justify="space-between" align="center" p={4} w="100%">
          <Box>CPS120 Showcase</Box>
          <ColorModeToggle />
        </Flex>
        <Tabs isFitted variant="enclosed" w="100%" index={tabIndex} onChange={handleTabsChange} className="cps120-chakra-tabs">
          <TabList className='cps120-chakra-tablist'>
            {tabData.map((tab, index) => (
              <Tab key={index}>{tab.name}</Tab>
            ))}
          </TabList>
          <TabPanels>
            {tabData.map((tab, index) => (
              <TabPanel key={index} className="cps120-tab-panel">
                <Suspense fallback={<Spinner />}>
                  {tabIndex === index && (
                    <Box h="100%">
                      {React.createElement(tab.component, { isActiveTab: tabIndex === index })}
                    </Box>
                  )}
                </Suspense>
              </TabPanel>
            ))}
          </TabPanels>
        </Tabs>
      </Flex>
      </WebSocketProvider>
    </ChakraProvider>
  );
  
}

export default App;
