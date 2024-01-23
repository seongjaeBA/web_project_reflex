/** @jsxImportSource @emotion/react */


import { Fragment, useCallback, useContext } from "react"
import { EventLoopContext, StateContexts } from "/utils/context"
import { Event, isTrue } from "/utils/state"
import { Button, HStack, Modal, ModalBody, ModalContent, ModalHeader, ModalOverlay, Text } from "@chakra-ui/react"
import "focus-visible/dist/focus-visible"
import { getEventURL } from "/utils/state.js"
import { HamburgerIcon } from "@chakra-ui/icons"




export function Fragment_fd0e7cb8f9fb4669a6805377d925fba0 () {
  const [addEvents, connectError] = useContext(EventLoopContext);


  return (
    <Fragment>
  {isTrue(connectError !== null) ? (
  <Fragment>
  <Modal isOpen={connectError !== null}>
  <ModalOverlay>
  <ModalContent>
  <ModalHeader>
  {`Connection Error`}
</ModalHeader>
  <ModalBody>
  <Text>
  {`Cannot connect to server: `}
  {(connectError !== null) ? connectError.message : ''}
  {`. Check if server is reachable at `}
  {getEventURL().href}
</Text>
</ModalBody>
</ModalContent>
</ModalOverlay>
</Modal>
</Fragment>
) : (
  <Fragment/>
)}
</Fragment>
  )
}

export function Hamburgericon_6570866a2ba901e4c82e1c3c60d2e714 () {
  const [addEvents, connectError] = useContext(EventLoopContext);

  const on_click_b4e2380389eee0fbe8a1d25e127a3835 = useCallback((_e) => addEvents([Event("state.chat_state.toggle_drawer", {})], (_e), {}), [addEvents, Event])

  return (
    <HamburgerIcon onClick={on_click_b4e2380389eee0fbe8a1d25e127a3835} sx={{"mr": 4, "cursor": "pointer"}}/>
  )
}

export function Hstack_2421a4a78a8b56960420b86d0641355e () {
  const state = useContext(StateContexts.state)


  return (
    <HStack sx={{"bg": isTrue((state.router.page.path === "/\\ubb34\\ube44 \\uc778\\ud48b") || (((state.router.page.path === "/") && "\\ubb34\\ube44 \\uc778\\ud48b") === "Home")) ? `#5535d4` : `transparent`, "color": isTrue((state.router.page.path === "/\\ubb34\\ube44 \\uc778\\ud48b") || (((state.router.page.path === "/") && "\\ubb34\\ube44 \\uc778\\ud48b") === "Home")) ? `#1A1060` : `#fff`, "borderRadius": "0.375rem", "boxShadow": "0px 0px 0px 1px rgba(84, 82, 95, 0.14)", "width": "100%", "paddingX": "1em", "alignItems": "center", "justifyContent": "space-between"}}>
  <Text>
  {`무비 인풋`}
</Text>
</HStack>
  )
}

export function Hstack_ed18a1f352e8210abaa2c6dca362617e () {
  const state = useContext(StateContexts.state)


  return (
    <HStack sx={{"bg": isTrue((state.router.page.path === "/\\uc774\\ubbf8\\uc9c0 \\uc0dd\\uc131") || (((state.router.page.path === "/") && "\\uc774\\ubbf8\\uc9c0 \\uc0dd\\uc131") === "Home")) ? `#5535d4` : `transparent`, "color": isTrue((state.router.page.path === "/\\uc774\\ubbf8\\uc9c0 \\uc0dd\\uc131") || (((state.router.page.path === "/") && "\\uc774\\ubbf8\\uc9c0 \\uc0dd\\uc131") === "Home")) ? `#1A1060` : `#fff`, "borderRadius": "0.375rem", "boxShadow": "0px 0px 0px 1px rgba(84, 82, 95, 0.14)", "width": "100%", "paddingX": "1em", "alignItems": "center", "justifyContent": "space-between"}}>
  <Text>
  {`이미지 생성`}
</Text>
</HStack>
  )
}

export function Hstack_f0074069fcecb1f304807c68a49434f3 () {
  const state = useContext(StateContexts.state)


  return (
    <HStack sx={{"bg": isTrue((state.router.page.path === "/\\ubb34\\ube44 \\ud14c\\uc774\\ube14") || (((state.router.page.path === "/") && "\\ubb34\\ube44 \\ud14c\\uc774\\ube14") === "Home")) ? `#5535d4` : `transparent`, "color": isTrue((state.router.page.path === "/\\ubb34\\ube44 \\ud14c\\uc774\\ube14") || (((state.router.page.path === "/") && "\\ubb34\\ube44 \\ud14c\\uc774\\ube14") === "Home")) ? `#1A1060` : `#fff`, "borderRadius": "0.375rem", "boxShadow": "0px 0px 0px 1px rgba(84, 82, 95, 0.14)", "width": "100%", "paddingX": "1em", "alignItems": "center", "justifyContent": "space-between"}}>
  <Text>
  {`무비 테이블`}
</Text>
</HStack>
  )
}

export function Hstack_bfedb602673dece30c85f5c8e85b3792 () {
  const state = useContext(StateContexts.state)


  return (
    <HStack sx={{"bg": isTrue((state.router.page.path === "/chatapp") || (((state.router.page.path === "/") && "ChatApp") === "Home")) ? `#5535d4` : `transparent`, "color": isTrue((state.router.page.path === "/chatapp") || (((state.router.page.path === "/") && "ChatApp") === "Home")) ? `#1A1060` : `#fff`, "borderRadius": "0.375rem", "boxShadow": "0px 0px 0px 1px rgba(84, 82, 95, 0.14)", "width": "100%", "paddingX": "1em", "alignItems": "center", "justifyContent": "space-between"}}>
  <Text>
  {`ChatApp`}
</Text>
</HStack>
  )
}

export function Hstack_18340389758835dd4b3083eadea84258 () {
  const state = useContext(StateContexts.state)


  return (
    <HStack sx={{"bg": isTrue((state.router.page.path === "/llm \\ubb38\\uc11c \\uc694\\uc57d") || (((state.router.page.path === "/") && "LLM \\ubb38\\uc11c \\uc694\\uc57d") === "Home")) ? `#5535d4` : `transparent`, "color": isTrue((state.router.page.path === "/llm \\ubb38\\uc11c \\uc694\\uc57d") || (((state.router.page.path === "/") && "LLM \\ubb38\\uc11c \\uc694\\uc57d") === "Home")) ? `#1A1060` : `#fff`, "borderRadius": "0.375rem", "boxShadow": "0px 0px 0px 1px rgba(84, 82, 95, 0.14)", "width": "100%", "paddingX": "1em", "alignItems": "center", "justifyContent": "space-between"}}>
  <Text>
  {`LLM 문서 요약`}
</Text>
</HStack>
  )
}

export function Hstack_2fd27de8245f5a3d591934bdef6e971b () {
  const state = useContext(StateContexts.state)


  return (
    <HStack sx={{"bg": isTrue((state.router.page.path === "/\\ud30c\\uc77c \\uc5c5\\ub85c\\ub4dc to me") || (((state.router.page.path === "/") && "\\ud30c\\uc77c \\uc5c5\\ub85c\\ub4dc to me") === "Home")) ? `#5535d4` : `transparent`, "color": isTrue((state.router.page.path === "/\\ud30c\\uc77c \\uc5c5\\ub85c\\ub4dc to me") || (((state.router.page.path === "/") && "\\ud30c\\uc77c \\uc5c5\\ub85c\\ub4dc to me") === "Home")) ? `#1A1060` : `#fff`, "borderRadius": "0.375rem", "boxShadow": "0px 0px 0px 1px rgba(84, 82, 95, 0.14)", "width": "100%", "paddingX": "1em", "alignItems": "center", "justifyContent": "space-between"}}>
  <Text>
  {`파일 업로드 to me`}
</Text>
</HStack>
  )
}

export function Button_ef2ecb52de7a33a0b7fdc47300cf1bc5 () {
  const [addEvents, connectError] = useContext(EventLoopContext);

  const on_click_bd3d8027df8c64630047a708c6d08e4f = useCallback((_e) => addEvents([Event("state.chat_state.toggle_modal", {})], (_e), {}), [addEvents, Event])

  return (
    <Button onClick={on_click_bd3d8027df8c64630047a708c6d08e4f} sx={{"bg": "#5535d4", "px": "4", "py": "2", "h": "auto", "shadow": "rgba(50, 50, 93, 0.25) 0px 50px 100px -20px, rgba(0, 0, 0, 0.3) 0px 30px 60px -30px, rgba(10, 37, 64, 0.35) 0px -2px 6px 0px inset;", "color": "#fff", "_hover": {"bg": "#4c2db3"}}}>
  {`+ New chat`}
</Button>
  )
}
