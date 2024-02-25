import React, { useState, Suspense } from 'react';
import { ChakraProvider, Box, Tab, TabList, Tabs, TabPanels, TabPanel, Flex, Spinner } from '@chakra-ui/react';
import theme from './theme/theme';
import './App.css';
import ColorModeToggle from './components/ColorModeToggle';

const ViewOne = React.lazy(() => import('./pages/CPS120/ViewOne'));
const StoreView = React.lazy(() => import('./pages/CPS120/StoreView'));
const GuessingGame = React.lazy(() => import('./pages/CPS120/GuessingGame/GuessingGame'));

const tabData = [
  { name: 'Tab 1', component: ViewOne },
  { name: 'Tab 2', component: StoreView },
  { name: 'Tab 3', component: GuessingGame },
];

function App() {
  const [tabIndex, setTabIndex] = useState(0);

  const handleTabsChange = (index) => {
    setTabIndex(index);
  };

  return (
    <ChakraProvider theme={theme}>
      <Flex direction="column" h="100vh">
        <Flex justify="space-between" align="center" p={4} w="100%">
          <Box>Title</Box>
          <ColorModeToggle />
        </Flex>
        <Tabs isFitted variant="enclosed" w="100%" index={tabIndex} onChange={handleTabsChange}>
          <TabList>
            {tabData.map((tab) => (
              <Tab key={tab.name}>{tab.name}</Tab>
            ))}
          </TabList>
          <TabPanels>
            {tabData.map((tab, index) => (
              <TabPanel key={tab.name}>
                <Suspense fallback={<Spinner />}>
                  {tabIndex === index && (
                    <Box borderWidth="2px" borderRadius="lg" p={4} shadow="sm" h="100%">
                      {React.createElement(tab.component, { isActiveTab: tabIndex === index })}
                    </Box>
                  )}
                </Suspense>
              </TabPanel>
            ))}
          </TabPanels>
        </Tabs>
      </Flex>
    </ChakraProvider>
  );
}

export default App;
