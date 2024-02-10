import { useColorMode, Switch, Flex, Text } from '@chakra-ui/react';

const ColorModeToggle = () => {
  const { colorMode, toggleColorMode } = useColorMode();
  return (
    <Flex align="center">
      <Text mr={2}>{colorMode === 'light' ? 'Light' : 'Dark'} Mode:</Text>
      <Switch isChecked={colorMode === 'dark'} onChange={toggleColorMode} />
    </Flex>
  );
};

export default ColorModeToggle;
