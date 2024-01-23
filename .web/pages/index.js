/** @jsxImportSource @emotion/react */


import { Fragment, useCallback, useContext } from "react"
import { Button_ef2ecb52de7a33a0b7fdc47300cf1bc5, Fragment_fd0e7cb8f9fb4669a6805377d925fba0, Hamburgericon_6570866a2ba901e4c82e1c3c60d2e714, Hstack_18340389758835dd4b3083eadea84258, Hstack_2421a4a78a8b56960420b86d0641355e, Hstack_2fd27de8245f5a3d591934bdef6e971b, Hstack_bfedb602673dece30c85f5c8e85b3792, Hstack_ed18a1f352e8210abaa2c6dca362617e, Hstack_f0074069fcecb1f304807c68a49434f3 } from "/utils/stateful_components"
import { AspectRatio, Avatar, Box, Button, Code, Container, Divider, Grid, Heading, HStack, Image as ChakraImage, Input, Link, ListItem, Menu, MenuButton, MenuDivider, MenuItem, MenuList, option, OrderedList, Select, Spacer, Text, UnorderedList, VStack } from "@chakra-ui/react"
import "@radix-ui/themes/styles.css"
import "focus-visible/dist/focus-visible"
import "katex/dist/katex.min.css"
import NextLink from "next/link"
import { ColorModeContext, EventLoopContext, StateContexts } from "/utils/context"
import { Theme as RadixThemesTheme } from "@radix-ui/themes"
import { Event, getRefValue, getRefValues, isTrue, set_val } from "/utils/state"
import { DebounceInput } from "react-debounce-input"
import ReactMarkdown from "react-markdown"
import remarkMath from "remark-math"
import remarkGfm from "remark-gfm"
import rehypeKatex from "rehype-katex"
import rehypeRaw from "rehype-raw"
import { PrismAsyncLight as SyntaxHighlighter } from "react-syntax-highlighter"
import oneLight from "react-syntax-highlighter/dist/cjs/styles/prism/one-light"
import oneDark from "react-syntax-highlighter/dist/cjs/styles/prism/one-dark"
import python from "react-syntax-highlighter/dist/cjs/languages/prism/python"
import NextHead from "next/head"



export function Select_e63d36085e34db900af2adf929e43ffe () {
  const [addEvents, connectError] = useContext(EventLoopContext);

  const on_change_1278fdcf53f69fffb9885347b6dd9dba = useCallback((_e0) => addEvents([Event("state.select_state.set_option", {value:_e0.target.value})], (_e0), {}), [addEvents, Event])

  return (
    <Select name={`Year`} onChange={on_change_1278fdcf53f69fffb9885347b6dd9dba} placeholder={`개봉년도`} sx={{"colorSchemes": "black"}}>
  <option value={1800}>
  {`1800`}
</option>
  <option value={1801}>
  {`1801`}
</option>
  <option value={1802}>
  {`1802`}
</option>
  <option value={1803}>
  {`1803`}
</option>
  <option value={1804}>
  {`1804`}
</option>
  <option value={1805}>
  {`1805`}
</option>
  <option value={1806}>
  {`1806`}
</option>
  <option value={1807}>
  {`1807`}
</option>
  <option value={1808}>
  {`1808`}
</option>
  <option value={1809}>
  {`1809`}
</option>
  <option value={1810}>
  {`1810`}
</option>
  <option value={1811}>
  {`1811`}
</option>
  <option value={1812}>
  {`1812`}
</option>
  <option value={1813}>
  {`1813`}
</option>
  <option value={1814}>
  {`1814`}
</option>
  <option value={1815}>
  {`1815`}
</option>
  <option value={1816}>
  {`1816`}
</option>
  <option value={1817}>
  {`1817`}
</option>
  <option value={1818}>
  {`1818`}
</option>
  <option value={1819}>
  {`1819`}
</option>
  <option value={1820}>
  {`1820`}
</option>
  <option value={1821}>
  {`1821`}
</option>
  <option value={1822}>
  {`1822`}
</option>
  <option value={1823}>
  {`1823`}
</option>
  <option value={1824}>
  {`1824`}
</option>
  <option value={1825}>
  {`1825`}
</option>
  <option value={1826}>
  {`1826`}
</option>
  <option value={1827}>
  {`1827`}
</option>
  <option value={1828}>
  {`1828`}
</option>
  <option value={1829}>
  {`1829`}
</option>
  <option value={1830}>
  {`1830`}
</option>
  <option value={1831}>
  {`1831`}
</option>
  <option value={1832}>
  {`1832`}
</option>
  <option value={1833}>
  {`1833`}
</option>
  <option value={1834}>
  {`1834`}
</option>
  <option value={1835}>
  {`1835`}
</option>
  <option value={1836}>
  {`1836`}
</option>
  <option value={1837}>
  {`1837`}
</option>
  <option value={1838}>
  {`1838`}
</option>
  <option value={1839}>
  {`1839`}
</option>
  <option value={1840}>
  {`1840`}
</option>
  <option value={1841}>
  {`1841`}
</option>
  <option value={1842}>
  {`1842`}
</option>
  <option value={1843}>
  {`1843`}
</option>
  <option value={1844}>
  {`1844`}
</option>
  <option value={1845}>
  {`1845`}
</option>
  <option value={1846}>
  {`1846`}
</option>
  <option value={1847}>
  {`1847`}
</option>
  <option value={1848}>
  {`1848`}
</option>
  <option value={1849}>
  {`1849`}
</option>
  <option value={1850}>
  {`1850`}
</option>
  <option value={1851}>
  {`1851`}
</option>
  <option value={1852}>
  {`1852`}
</option>
  <option value={1853}>
  {`1853`}
</option>
  <option value={1854}>
  {`1854`}
</option>
  <option value={1855}>
  {`1855`}
</option>
  <option value={1856}>
  {`1856`}
</option>
  <option value={1857}>
  {`1857`}
</option>
  <option value={1858}>
  {`1858`}
</option>
  <option value={1859}>
  {`1859`}
</option>
  <option value={1860}>
  {`1860`}
</option>
  <option value={1861}>
  {`1861`}
</option>
  <option value={1862}>
  {`1862`}
</option>
  <option value={1863}>
  {`1863`}
</option>
  <option value={1864}>
  {`1864`}
</option>
  <option value={1865}>
  {`1865`}
</option>
  <option value={1866}>
  {`1866`}
</option>
  <option value={1867}>
  {`1867`}
</option>
  <option value={1868}>
  {`1868`}
</option>
  <option value={1869}>
  {`1869`}
</option>
  <option value={1870}>
  {`1870`}
</option>
  <option value={1871}>
  {`1871`}
</option>
  <option value={1872}>
  {`1872`}
</option>
  <option value={1873}>
  {`1873`}
</option>
  <option value={1874}>
  {`1874`}
</option>
  <option value={1875}>
  {`1875`}
</option>
  <option value={1876}>
  {`1876`}
</option>
  <option value={1877}>
  {`1877`}
</option>
  <option value={1878}>
  {`1878`}
</option>
  <option value={1879}>
  {`1879`}
</option>
  <option value={1880}>
  {`1880`}
</option>
  <option value={1881}>
  {`1881`}
</option>
  <option value={1882}>
  {`1882`}
</option>
  <option value={1883}>
  {`1883`}
</option>
  <option value={1884}>
  {`1884`}
</option>
  <option value={1885}>
  {`1885`}
</option>
  <option value={1886}>
  {`1886`}
</option>
  <option value={1887}>
  {`1887`}
</option>
  <option value={1888}>
  {`1888`}
</option>
  <option value={1889}>
  {`1889`}
</option>
  <option value={1890}>
  {`1890`}
</option>
  <option value={1891}>
  {`1891`}
</option>
  <option value={1892}>
  {`1892`}
</option>
  <option value={1893}>
  {`1893`}
</option>
  <option value={1894}>
  {`1894`}
</option>
  <option value={1895}>
  {`1895`}
</option>
  <option value={1896}>
  {`1896`}
</option>
  <option value={1897}>
  {`1897`}
</option>
  <option value={1898}>
  {`1898`}
</option>
  <option value={1899}>
  {`1899`}
</option>
  <option value={1900}>
  {`1900`}
</option>
  <option value={1901}>
  {`1901`}
</option>
  <option value={1902}>
  {`1902`}
</option>
  <option value={1903}>
  {`1903`}
</option>
  <option value={1904}>
  {`1904`}
</option>
  <option value={1905}>
  {`1905`}
</option>
  <option value={1906}>
  {`1906`}
</option>
  <option value={1907}>
  {`1907`}
</option>
  <option value={1908}>
  {`1908`}
</option>
  <option value={1909}>
  {`1909`}
</option>
  <option value={1910}>
  {`1910`}
</option>
  <option value={1911}>
  {`1911`}
</option>
  <option value={1912}>
  {`1912`}
</option>
  <option value={1913}>
  {`1913`}
</option>
  <option value={1914}>
  {`1914`}
</option>
  <option value={1915}>
  {`1915`}
</option>
  <option value={1916}>
  {`1916`}
</option>
  <option value={1917}>
  {`1917`}
</option>
  <option value={1918}>
  {`1918`}
</option>
  <option value={1919}>
  {`1919`}
</option>
  <option value={1920}>
  {`1920`}
</option>
  <option value={1921}>
  {`1921`}
</option>
  <option value={1922}>
  {`1922`}
</option>
  <option value={1923}>
  {`1923`}
</option>
  <option value={1924}>
  {`1924`}
</option>
  <option value={1925}>
  {`1925`}
</option>
  <option value={1926}>
  {`1926`}
</option>
  <option value={1927}>
  {`1927`}
</option>
  <option value={1928}>
  {`1928`}
</option>
  <option value={1929}>
  {`1929`}
</option>
  <option value={1930}>
  {`1930`}
</option>
  <option value={1931}>
  {`1931`}
</option>
  <option value={1932}>
  {`1932`}
</option>
  <option value={1933}>
  {`1933`}
</option>
  <option value={1934}>
  {`1934`}
</option>
  <option value={1935}>
  {`1935`}
</option>
  <option value={1936}>
  {`1936`}
</option>
  <option value={1937}>
  {`1937`}
</option>
  <option value={1938}>
  {`1938`}
</option>
  <option value={1939}>
  {`1939`}
</option>
  <option value={1940}>
  {`1940`}
</option>
  <option value={1941}>
  {`1941`}
</option>
  <option value={1942}>
  {`1942`}
</option>
  <option value={1943}>
  {`1943`}
</option>
  <option value={1944}>
  {`1944`}
</option>
  <option value={1945}>
  {`1945`}
</option>
  <option value={1946}>
  {`1946`}
</option>
  <option value={1947}>
  {`1947`}
</option>
  <option value={1948}>
  {`1948`}
</option>
  <option value={1949}>
  {`1949`}
</option>
  <option value={1950}>
  {`1950`}
</option>
  <option value={1951}>
  {`1951`}
</option>
  <option value={1952}>
  {`1952`}
</option>
  <option value={1953}>
  {`1953`}
</option>
  <option value={1954}>
  {`1954`}
</option>
  <option value={1955}>
  {`1955`}
</option>
  <option value={1956}>
  {`1956`}
</option>
  <option value={1957}>
  {`1957`}
</option>
  <option value={1958}>
  {`1958`}
</option>
  <option value={1959}>
  {`1959`}
</option>
  <option value={1960}>
  {`1960`}
</option>
  <option value={1961}>
  {`1961`}
</option>
  <option value={1962}>
  {`1962`}
</option>
  <option value={1963}>
  {`1963`}
</option>
  <option value={1964}>
  {`1964`}
</option>
  <option value={1965}>
  {`1965`}
</option>
  <option value={1966}>
  {`1966`}
</option>
  <option value={1967}>
  {`1967`}
</option>
  <option value={1968}>
  {`1968`}
</option>
  <option value={1969}>
  {`1969`}
</option>
  <option value={1970}>
  {`1970`}
</option>
  <option value={1971}>
  {`1971`}
</option>
  <option value={1972}>
  {`1972`}
</option>
  <option value={1973}>
  {`1973`}
</option>
  <option value={1974}>
  {`1974`}
</option>
  <option value={1975}>
  {`1975`}
</option>
  <option value={1976}>
  {`1976`}
</option>
  <option value={1977}>
  {`1977`}
</option>
  <option value={1978}>
  {`1978`}
</option>
  <option value={1979}>
  {`1979`}
</option>
  <option value={1980}>
  {`1980`}
</option>
  <option value={1981}>
  {`1981`}
</option>
  <option value={1982}>
  {`1982`}
</option>
  <option value={1983}>
  {`1983`}
</option>
  <option value={1984}>
  {`1984`}
</option>
  <option value={1985}>
  {`1985`}
</option>
  <option value={1986}>
  {`1986`}
</option>
  <option value={1987}>
  {`1987`}
</option>
  <option value={1988}>
  {`1988`}
</option>
  <option value={1989}>
  {`1989`}
</option>
  <option value={1990}>
  {`1990`}
</option>
  <option value={1991}>
  {`1991`}
</option>
  <option value={1992}>
  {`1992`}
</option>
  <option value={1993}>
  {`1993`}
</option>
  <option value={1994}>
  {`1994`}
</option>
  <option value={1995}>
  {`1995`}
</option>
  <option value={1996}>
  {`1996`}
</option>
  <option value={1997}>
  {`1997`}
</option>
  <option value={1998}>
  {`1998`}
</option>
  <option value={1999}>
  {`1999`}
</option>
  <option value={2000}>
  {`2000`}
</option>
  <option value={2001}>
  {`2001`}
</option>
  <option value={2002}>
  {`2002`}
</option>
  <option value={2003}>
  {`2003`}
</option>
  <option value={2004}>
  {`2004`}
</option>
  <option value={2005}>
  {`2005`}
</option>
  <option value={2006}>
  {`2006`}
</option>
  <option value={2007}>
  {`2007`}
</option>
  <option value={2008}>
  {`2008`}
</option>
  <option value={2009}>
  {`2009`}
</option>
  <option value={2010}>
  {`2010`}
</option>
  <option value={2011}>
  {`2011`}
</option>
  <option value={2012}>
  {`2012`}
</option>
  <option value={2013}>
  {`2013`}
</option>
  <option value={2014}>
  {`2014`}
</option>
  <option value={2015}>
  {`2015`}
</option>
  <option value={2016}>
  {`2016`}
</option>
  <option value={2017}>
  {`2017`}
</option>
  <option value={2018}>
  {`2018`}
</option>
  <option value={2019}>
  {`2019`}
</option>
  <option value={2020}>
  {`2020`}
</option>
  <option value={2021}>
  {`2021`}
</option>
  <option value={2022}>
  {`2022`}
</option>
  <option value={2023}>
  {`2023`}
</option>
  <option value={2024}>
  {`2024`}
</option>
  <option value={2025}>
  {`2025`}
</option>
  <option value={2026}>
  {`2026`}
</option>
  <option value={2027}>
  {`2027`}
</option>
</Select>
  )
}

        function ComponentMap_0fb8c7bde874ca761b52e7c8e8eb76d3 () {
            const [ colorMode, toggleColorMode ] = useContext(ColorModeContext)
            return (
                {"h1": ({node, children, ...props}) => <Heading as={`h1`} size={`2xl`} sx={{"marginY": "0.5em"}} {...props}>   {children} </Heading>, "h2": ({node, children, ...props}) => <Heading as={`h2`} size={`xl`} sx={{"marginY": "0.5em"}} {...props}>   {children} </Heading>, "h3": ({node, children, ...props}) => <Heading as={`h3`} size={`lg`} sx={{"marginY": "0.5em"}} {...props}>   {children} </Heading>, "h4": ({node, children, ...props}) => <Heading as={`h4`} size={`md`} sx={{"marginY": "0.5em"}} {...props}>   {children} </Heading>, "h5": ({node, children, ...props}) => <Heading as={`h5`} size={`sm`} sx={{"marginY": "0.5em"}} {...props}>   {children} </Heading>, "h6": ({node, children, ...props}) => <Heading as={`h6`} size={`xs`} sx={{"marginY": "0.5em"}} {...props}>   {children} </Heading>, "p": ({node, children, ...props}) => <Text sx={{"marginY": "1em"}} {...props}>   {children} </Text>, "ul": ({node, children, ...props}) => <UnorderedList sx={{"marginY": "1em"}}>   {children} </UnorderedList>, "ol": ({node, children, ...props}) => <OrderedList sx={{"marginY": "1em"}}>   {children} </OrderedList>, "li": ({node, children, ...props}) => <ListItem sx={{"marginY": "0.5em"}}>   {children} </ListItem>, "a": ({node, children, ...props}) => <Link as={``} {...props}>   {children} </Link>, "code": ({node, inline, className, children, ...props}) => {     const match = (className || '').match(/language-(?<lang>.*)/);     const language = match ? match[1] : '';     if (language) {     (async () => {       try {         const module = await import(`react-syntax-highlighter/dist/cjs/languages/prism/${language}`);         SyntaxHighlighter.registerLanguage(language, module.default);       } catch (error) {         console.error(`Error importing language module for ${language}:`, error);       }     })();   }     return inline ? (         <Code {...props}>   {children} </Code>     ) : (         <SyntaxHighlighter css={{"marginY": "1em"}} customStyle={{"marginY": "1em"}} language={language} style={isTrue((colorMode === "light")) ? oneLight : oneDark} {...props} children={children}/>     );       }, "codeblock": ({node, children, ...props}) => <SyntaxHighlighter css={{"marginY": "1em"}} customStyle={{"marginY": "1em"}} language={`python`} style={isTrue((colorMode === "light")) ? oneLight : oneDark} {...props} children={children}/>}
            )
        }
        

export function Debounceinput_73a27235f782ee73e3648a83b6a3d9c2 () {
  const [addEvents, connectError] = useContext(EventLoopContext);
  const state__crud_state__query_state = useContext(StateContexts.state__crud_state__query_state)

  const on_change_7eb2d699660bdb388e8c7103aef5460e = useCallback((_e0) => addEvents([Event("state.crud_state.query_state.set_url_query", {value:_e0.target.value})], (_e0), {}), [addEvents, Event])

  return (
    <DebounceInput debounceTimeout={50} element={Input} onChange={on_change_7eb2d699660bdb388e8c7103aef5460e} sx={{"width": "30vw"}} type={`text`} value={state__crud_state__query_state.url_query}/>
  )
}

export function Select_ba6ff6e1e32113ecad07c283b33c7112 () {
  const [addEvents, connectError] = useContext(EventLoopContext);

  const on_change_d9065ec66b3816ff065bfd017f603fba = useCallback((_e0) => addEvents([Event("state.crud_state.query_state.update_method", {value:_e0.target.value})], (_e0), {}), [addEvents, Event])

  return (
    <Select onChange={on_change_d9065ec66b3816ff065bfd017f603fba}>
  <option value={`GET`}>
  {`GET`}
</option>
  <option value={`POST`}>
  {`POST`}
</option>
  <option value={`PUT`}>
  {`PUT`}
</option>
  <option value={`DELETE`}>
  {`DELETE`}
</option>
</Select>
  )
}

export function Text_1080eb91387b56c958b1db989df13fcd () {
  const state__form_state = useContext(StateContexts.state__form_state)


  return (
    <Text>
  {JSON.stringify(state__form_state.form_data)}
</Text>
  )
}

export function Box_8c6a298a642ea47f44e50d6bb7b585a6 () {
  
    const handleSubmit_4038683695e0e6eb8e2a554ff648ff40 = useCallback((ev) => {
        const $form = ev.target
        ev.preventDefault()
        const form_data = {...Object.fromEntries(new FormData($form).entries()), ...{}}

        addEvents([Event("state.form_state.handle_submit", {form_data:form_data})])

        if (true) {
            $form.reset()
        }
    })
    
  const [addEvents, connectError] = useContext(EventLoopContext);


  return (
    <Box as={`form`} onSubmit={handleSubmit_4038683695e0e6eb8e2a554ff648ff40}>
  <VStack sx={{"alignItems": "stretch", "justifyContent": "space-between"}}>
  <Input name={`MovieCode`} placeholder={`Movie Code`} sx={{"bg": "#111"}} type={`text`}/>
  <Input name={`Title`} placeholder={`제목`} sx={{"bg": "#111"}} type={`text`}/>
  <Input name={`image`} placeholder={`image`} sx={{"bg": "#111"}} type={`text`}/>
  <Select_e63d36085e34db900af2adf929e43ffe/>
  <Input name={`Genre`} placeholder={`장르`} sx={{"bg": "#111"}} type={`text`}/>
  <Input name={`Director`} placeholder={`감독`} sx={{"bg": "#111"}} type={`text`}/>
  <Input name={`Actors`} placeholder={`배우`} sx={{"bg": "#111"}} type={`submit`}/>
  <HStack sx={{"alignItems": "center", "justifyContent": "space-between"}}>
  <Button_5f2988c43c4060778e94963bb9bdd476/>
  <Button_59dfc414ac72c81b75d3b26b2e81d16d/>
</HStack>
</VStack>
</Box>
  )
}

export function Button_59dfc414ac72c81b75d3b26b2e81d16d () {
  const [addEvents, connectError] = useContext(EventLoopContext);

  const on_click_344a0c169a6c735deb4c53ad5bcf9ff0 = useCallback((_e) => addEvents([Event("state.crud_state.query_state.send_query", {})], (_e), {}), [addEvents, Event])

  return (
    <Button onClick={on_click_344a0c169a6c735deb4c53ad5bcf9ff0} sx={{"shadow": "rgba(50, 50, 93, 0.25) 0px 50px 100px -20px, rgba(0, 0, 0, 0.3) 0px 30px 60px -30px, rgba(10, 37, 64, 0.35) 0px -2px 6px 0px inset;", "color": "#fff", "_hover": {"bg": "#4c2db3"}}}>
  {`Send`}
</Button>
  )
}

export function Heading_3e018c6e93b69fa507881f7c54a7e7ca () {
  const state__crud_state = useContext(StateContexts.state__crud_state)


  return (
    <Heading sx={{"color": "black"}}>
  {state__crud_state.total}
  {` : Movie found`}
</Heading>
  )
}

export function Vstack_c8d829b38101b6ca61a821aa8f8619e3 () {
  const state__crud_state = useContext(StateContexts.state__crud_state)


  return (
    <VStack sx={{"width": "30vw", "height": "100vh", "bg": "white", "alignItems": "stretch", "justifyContent": "space-between"}}>
  <Heading_3e018c6e93b69fa507881f7c54a7e7ca/>
  {state__crud_state.movies.map((movie, index_812bbb3bea220c366d62b4943220e837) => (
  <AspectRatio key={index_812bbb3bea220c366d62b4943220e837}>
  <HStack sx={{"border": "solid black 1px", "spcaing": "5", "width": "100%"}}>
  <ChakraImage src={movie.image} sx={{"width": "3vw"}}/>
  <Text sx={{"width": "10vw", "color": "rgb(107,99,246)"}}>
  {`(${movie.MovieCode}) ${movie.Title}`}
</Text>
  <VStack spacing={`0`} sx={{"width": "7vw"}}>
  <Text sx={{"color": "rgb(107,99,246)"}}>
  {`Year:`}
  {movie.Year}
</Text>
  <Text sx={{"color": "rgb(107,99,246)"}}>
  {`Genre:`}
  {movie.Genre}
</Text>
</VStack>
  <VStack spacing={`0`} sx={{"width": "7vw"}}>
  <Text sx={{"color": "rgb(107,99,246)"}}>
  {`Director:`}
  {movie.Director}
</Text>
  <Text sx={{"color": "rgb(107,99,246)"}}>
  {`Actors:`}
  {movie.Actors}
</Text>
</VStack>
  <Spacer/>
</HStack>
</AspectRatio>
))}
  <Spacer/>
</VStack>
  )
}

export function Reactmarkdown_e963132a5df32c9695b5f10d8dbe50ba () {
  const state__crud_state__query_state = useContext(StateContexts.state__crud_state__query_state)


  return (
    <ReactMarkdown css={{"language": "json", "height": "30vh"}} rehypePlugins={[rehypeKatex, rehypeRaw]} remarkPlugins={[remarkMath, remarkGfm]} components={ComponentMap_0fb8c7bde874ca761b52e7c8e8eb76d3()}>
  {state__crud_state__query_state.f_response}
</ReactMarkdown>
  )
}

export function Button_5f2988c43c4060778e94963bb9bdd476 () {
  const [addEvents, connectError] = useContext(EventLoopContext);

  const on_click_673eaf83976a611e659d953997f56aff = useCallback((_e) => addEvents([Event("state.crud_state.query_state.clear_query", {})], (_e), {}), [addEvents, Event])

  return (
    <Button onClick={on_click_673eaf83976a611e659d953997f56aff} sx={{"shadow": "rgba(50, 50, 93, 0.25) 0px 50px 100px -20px, rgba(0, 0, 0, 0.3) 0px 30px 60px -30px, rgba(10, 37, 64, 0.35) 0px -2px 6px 0px inset;", "color": "#fff", "_hover": {"bg": "#4c2db3"}}}>
  {`Clear`}
</Button>
  )
}

export function Text_7c0669faf5b975bbcbad1b6c0361bd92 () {
  const state__crud_state__query_state = useContext(StateContexts.state__crud_state__query_state)


  return (
    <Text>
  {`Status: `}
  {state__crud_state__query_state.response_code}
</Text>
  )
}

export default function Component() {

  return (
    <Fragment>
  <Fragment_fd0e7cb8f9fb4669a6805377d925fba0/>
  <VStack alignItems={`stretch`} spacing={`0`} sx={{"transition": "left 0.5s, width 0.5s", "bg": "#111", "color": "#fff", "minH": "100vh", "width": "100vw", "alignItems": "stretch", "justifyContent": "space-between"}}>
  <Grid sx={{"bg": "#111", "backdropFilter": "auto", "backdropBlur": "lg", "p": "4", "borderBottom": "1px solid #fff3", "position": "sticky", "top": "0", "zIndex": "100"}}>
  <HStack justify={`space-between`} sx={{"minWidth": "10em", "height": "100%", "position": "sticky", "top": "0px", "borderRight": {"border": "2px solid black", "color": "black"}, "alignItems": "center", "justifyContent": "space-between"}}>
  <HStack sx={{"alignItems": "center", "justifyContent": "space-between"}}>
  <Spacer/>
  <Hamburgericon_6570866a2ba901e4c82e1c3c60d2e714/>
</HStack>
  <HStack alignItems={`flex-start`} sx={{"overflowY": "auto", "padding": "1em", "alignItems": "center", "justifyContent": "space-between"}}>
  <Link as={NextLink} href={`/`} sx={{"width": "100%"}}>
  <Hstack_2421a4a78a8b56960420b86d0641355e/>
</Link>
  <Link as={NextLink} href={`/Dalle`} sx={{"width": "100%"}}>
  <Hstack_ed18a1f352e8210abaa2c6dca362617e/>
</Link>
  <Link as={NextLink} href={`/MovieTable`} sx={{"width": "100%"}}>
  <Hstack_f0074069fcecb1f304807c68a49434f3/>
</Link>
  <Link as={NextLink} href={`/chatapp`} sx={{"width": "100%"}}>
  <Hstack_bfedb602673dece30c85f5c8e85b3792/>
</Link>
  <Link as={NextLink} href={`/summarizer`} sx={{"width": "100%"}}>
  <Hstack_18340389758835dd4b3083eadea84258/>
</Link>
  <Link as={NextLink} href={`/upload`} sx={{"width": "100%"}}>
  <Hstack_2fd27de8245f5a3d591934bdef6e971b/>
</Link>
</HStack>
  <Spacer/>
  <HStack spacing={`8`} sx={{"alignItems": "center", "justifyContent": "space-between"}}>
  <Button_ef2ecb52de7a33a0b7fdc47300cf1bc5/>
  <Menu sx={{"bg": "#111", "border": "red"}}>
  <MenuButton>
  <Avatar name={`User`} size={`md`} sx={{"shadow": "rgba(50, 50, 93, 0.25) 0px 50px 100px -20px, rgba(0, 0, 0, 0.3) 0px 30px 60px -30px, rgba(10, 37, 64, 0.35) 0px -2px 6px 0px inset;", "color": "#fff", "bg": "#fff3"}}/>
  <Box/>
</MenuButton>
  <MenuList sx={{"bg": "#111", "border": "1.5px solid #222"}}>
  <MenuItem sx={{"bg": "#111", "color": "#fff"}}>
  {`Help`}
</MenuItem>
  <MenuDivider sx={{"border": "1px solid #222"}}/>
  <MenuItem sx={{"bg": "#111", "color": "#fff"}}>
  {`Settings`}
</MenuItem>
</MenuList>
</Menu>
</HStack>
</HStack>
</Grid>
  <HStack alignItems={`flex-start`} sx={{"paddingTop": "5em", "paddingX": ["auto", "2em"], "flex": "1", "position": "relative", "alignItems": "center", "justifyContent": "space-between"}}>
  <Box sx={{"boxShadow": "0px 0px 0px 1px rgba(84, 82, 95, 0.14)", "borderRadius": "0.375rem", "padding": "1em", "marginBottom": "2em"}}>
  <HStack spacing={`0`} sx={{"height": "100%", "width": "100vw", "alignItems": "center", "justifyContent": "space-between"}}>
  <Vstack_c8d829b38101b6ca61a821aa8f8619e3/>
  <Spacer/>
  <Divider orientation={`vertical`} sx={{"border": "solid black 1px"}}/>
  <VStack sx={{"width": "50vw", "alignItems": "stretch", "justifyContent": "space-between"}}>
  <HStack sx={{"alignItems": "center", "justifyContent": "space-between"}}>
  <Text>
  {`검색 조건:`}
</Text>
  <Select_ba6ff6e1e32113ecad07c283b33c7112/>
  <Debounceinput_73a27235f782ee73e3648a83b6a3d9c2/>
</HStack>
  <Box_8c6a298a642ea47f44e50d6bb7b585a6/>
  <Divider orientation={`horizontal`} sx={{"border": "solid black 1px", "width": "100%"}}/>
  <HStack sx={{"width": "100%", "alignItems": "center", "justifyContent": "space-between"}}>
  <Text_7c0669faf5b975bbcbad1b6c0361bd92/>
  <Spacer/>
</HStack>
  <Container>
  <Text_1080eb91387b56c958b1db989df13fcd/>
</Container>
  <Container>
  <Reactmarkdown_e963132a5df32c9695b5f10d8dbe50ba/>
</Container>
</VStack>
  <Spacer/>
</HStack>
</Box>
</HStack>
</VStack>
  <NextHead>
  <title>
  {`무비 인풋`}
</title>
  <meta content={`A Reflex app.`} name={`description`}/>
  <meta content={`favicon.ico`} property={`og:image`}/>
  <meta content={`width=device-width, shrink-to-fit=no, initial-scale=1`} name={`viewport`}/>
</NextHead>
</Fragment>
  )
}
