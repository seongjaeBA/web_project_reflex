/** @jsxImportSource @emotion/react */


import { Fragment, useCallback, useContext } from "react"
import { Fragment_fd0e7cb8f9fb4669a6805377d925fba0, Hstack_82c2a003386503f0becf4fea458939f6, Hstack_ab4794008275880551112d3b8dc3895c, Hstack_bad9a923cbf0b3070367eb5f3fcbaee0, Hstack_c09c0f536ed0a484ab952882270ec40a } from "/utils/stateful_components"
import { Box, Button, Center, Container, HStack, Image as ChakraImage, Input, Link, Menu, MenuButton, MenuDivider, MenuItem, MenuList, Spacer, Text, VStack } from "@chakra-ui/react"
import NextLink from "next/link"
import "@radix-ui/themes/styles.css"
import "focus-visible/dist/focus-visible"
import { Theme as RadixThemesTheme } from "@radix-ui/themes"
import { EventLoopContext, StateContexts } from "/utils/context"
import { DebounceInput } from "react-debounce-input"
import { Event, set_val } from "/utils/state"
import { HamburgerIcon } from "@chakra-ui/icons"
import NextHead from "next/head"



export function Debounceinput_a68d39e9ce9ca02bb5fcd84ec8de41a7 () {
  const state__open_state = useContext(StateContexts.state__open_state)
  const [addEvents, connectError] = useContext(EventLoopContext);

  const on_change_3cee39bde4b5c56352ccf9c403610050 = useCallback((_e0) => addEvents([Event("state.open_state.set_question", {value:_e0.target.value})], (_e0), {}), [addEvents, Event])

  return (
    <DebounceInput debounceTimeout={50} element={Input} onChange={on_change_3cee39bde4b5c56352ccf9c403610050} placeholder={`Ask a question`} sx={{"borderWidth": "1px", "padding": "1em", "boxShadow": "rgba(0, 0, 0, 0.15) 0px 2px 8px"}} type={`text`} value={state__open_state.question}/>
  )
}

export function Button_c4949e16ccb2bbab439481e9e8317711 () {
  const [addEvents, connectError] = useContext(EventLoopContext);

  const on_click_61a6ce3676a36ac193c8b4838f26459c = useCallback((_e) => addEvents([Event("state.open_state.answer", {})], (_e), {}), [addEvents, Event])

  return (
    <Button onClick={on_click_61a6ce3676a36ac193c8b4838f26459c} sx={{"bg": "#CEFFEE", "boxShadow": "rgba(0, 0, 0, 0.15) 0px 2px 8px"}}>
  {`Ask`}
</Button>
  )
}

export function Box_4e5887e7a8a5dab97db075c77b4af61b () {
  const state__open_state = useContext(StateContexts.state__open_state)


  return (
    <Box>
  {state__open_state.chat_history.map((messages, index_205bac7b9f5ee2daa713c994b321f268) => (
  <Box key={index_205bac7b9f5ee2daa713c994b321f268} sx={{"marginY": "1em"}}>
  <Box sx={{"padding": "1em", "borderRadius": "5px", "marginY": "0.5em", "boxShadow": "rgba(0, 0, 0, 0.15) 0px 2px 8px", "bg": "#F5EFFE", "marginLeft": "20%"}}>
  <Text sx={{"textAlign": "right"}}>
  {messages.at(0)}
</Text>
</Box>
  <Box sx={{"padding": "1em", "borderRadius": "5px", "marginY": "0.5em", "boxShadow": "rgba(0, 0, 0, 0.15) 0px 2px 8px", "bg": "#DEEAFD", "marginRight": "20%"}}>
  <Text sx={{"textAlign": "left"}}>
  {messages.at(1)}
</Text>
</Box>
</Box>
))}
</Box>
  )
}

export default function Component() {

  return (
    <Fragment>
  <Fragment_fd0e7cb8f9fb4669a6805377d925fba0/>
  <HStack alignItems={`flex-start`} sx={{"transition": "left 0.5s, width 0.5s", "position": "relative"}}>
  <Box sx={{"display": ["none", "none", "block"], "minWidth": "20em", "height": "100%", "position": "sticky", "top": "0px", "borderRight": "1px solid #F4F3F6"}}>
  <VStack sx={{"height": "100dvh"}}>
  <HStack sx={{"width": "100%", "borderBottom": "1px solid #F4F3F6", "padding": "1em"}}>
  <Link as={NextLink} href={`https://www.hi-str.com/`}>
  <Text>
  {`cineinsight`}
</Text>
</Link>
  <Spacer/>
  <Link as={NextLink} href={`https://www.hi-str.com/`}>
  <Center sx={{"boxShadow": "0px 0px 0px 1px rgba(84, 82, 95, 0.14)", "bg": "transparent", "borderRadius": "0.375rem", "_hover": {"bg": "#F5EFFE"}}}>
  <ChakraImage src={`/logo.png`} sx={{"height": "3em", "padding": "0.5em"}}/>
</Center>
</Link>
</HStack>
  <VStack alignItems={`flex-start`} sx={{"width": "100%", "overflowY": "auto", "padding": "1em"}}>
  <Link as={NextLink} href={`/`} sx={{"width": "100%"}}>
  <Hstack_bad9a923cbf0b3070367eb5f3fcbaee0/>
</Link>
  <Link as={NextLink} href={`/dashboard`} sx={{"width": "100%"}}>
  <Hstack_c09c0f536ed0a484ab952882270ec40a/>
</Link>
  <Link as={NextLink} href={`/settings`} sx={{"width": "100%"}}>
  <Hstack_82c2a003386503f0becf4fea458939f6/>
</Link>
  <Link as={NextLink} href={`/treatment-gen`} sx={{"width": "100%"}}>
  <Hstack_ab4794008275880551112d3b8dc3895c/>
</Link>
</VStack>
  <Spacer/>
  <HStack sx={{"width": "100%", "borderTop": "1px solid #F4F3F6", "padding": "1em"}}>
  <Spacer/>
  <Link as={NextLink} href={`https://www.hi-str.com/`}>
  <Text>
  {`Docs`}
</Text>
</Link>
  <Link as={NextLink} href={`https://www.hi-str.com/`}>
  <Text>
  {`Blog`}
</Text>
</Link>
</HStack>
</VStack>
</Box>
  <Box sx={{"paddingTop": "5em", "paddingX": ["auto", "2em"], "flex": "1"}}>
  <Box sx={{"alignItems": "flex-start", "boxShadow": "0px 0px 0px 1px rgba(84, 82, 95, 0.14)", "borderRadius": "0.375rem", "padding": "1em", "marginBottom": "2em"}}>
  <Container>
  <Box_4e5887e7a8a5dab97db075c77b4af61b/>
  <HStack>
  <Debounceinput_a68d39e9ce9ca02bb5fcd84ec8de41a7/>
  <Button_c4949e16ccb2bbab439481e9e8317711/>
</HStack>
</Container>
</Box>
</Box>
  <Box sx={{"position": "fixed", "right": "1.5em", "top": "1.5em", "zIndex": "500"}}>
  <Menu>
  <MenuButton sx={{"width": "3em", "height": "3em", "backgroundColor": "white", "border": "1px solid #F4F3F6", "borderRadius": "0.375rem"}}>
  <HamburgerIcon sx={{"size": "4em", "color": "black"}}/>
</MenuButton>
  <MenuList>
  <MenuItem sx={{"_hover": {"bg": "#F5EFFE"}}}>
  <Link as={NextLink} href={`/`} sx={{"width": "100%"}}>
  {`Home`}
</Link>
</MenuItem>
  <MenuItem sx={{"_hover": {"bg": "#F5EFFE"}}}>
  <Link as={NextLink} href={`/dashboard`} sx={{"width": "100%"}}>
  {`Dashboard`}
</Link>
</MenuItem>
  <MenuItem sx={{"_hover": {"bg": "#F5EFFE"}}}>
  <Link as={NextLink} href={`/settings`} sx={{"width": "100%"}}>
  {`Settings`}
</Link>
</MenuItem>
  <MenuItem sx={{"_hover": {"bg": "#F5EFFE"}}}>
  <Link as={NextLink} href={`/treatment-gen`} sx={{"width": "100%"}}>
  {`Treatment Generate`}
</Link>
</MenuItem>
  <MenuDivider/>
  <MenuItem sx={{"_hover": {"bg": "#F5EFFE"}}}>
  <Link as={NextLink} href={`https://www.hi-str.com/`} sx={{"width": "100%"}}>
  {`About`}
</Link>
</MenuItem>
  <MenuItem sx={{"_hover": {"bg": "#F5EFFE"}}}>
  <Link as={NextLink} href={`mailto:cs@hi-str.com`} sx={{"width": "100%"}}>
  {`Contact`}
</Link>
</MenuItem>
</MenuList>
</Menu>
</Box>
</HStack>
  <NextHead>
  <title>
  {`Treatment Generate`}
</title>
  <meta content={`A Reflex app.`} name={`description`}/>
  <meta content={`favicon.ico`} property={`og:image`}/>
  <meta content={`width=device-width, shrink-to-fit=no, initial-scale=1`} name={`viewport`}/>
</NextHead>
</Fragment>
  )
}
