import { createContext, useContext, useMemo, useReducer, useState } from "react"
import { applyDelta, Event, hydrateClientStorage, useEventLoop, refs } from "/utils/state.js"

export const initialState = {"state": {"is_hydrated": false, "router": {"session": {"client_token": "", "client_ip": "", "session_id": ""}, "headers": {"host": "", "origin": "", "upgrade": "", "connection": "", "pragma": "", "cache_control": "", "user_agent": "", "sec_websocket_version": "", "sec_websocket_key": "", "sec_websocket_extensions": "", "accept_encoding": "", "accept_language": ""}, "page": {"host": "", "path": "", "raw_path": "", "full_path": "", "full_raw_path": "", "params": {}}}}, "state.open_state": {"chat_history": [], "question": ""}, "state.lanchain_state": {"is_loading": false, "large_text": "", "loading_text": "", "openai_api_key": "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", "summary": ""}, "state.base_state": {}, "state.base_state.kmdb_table_live_state": {"KMDB_API": "5NUU48I7L0P8233U83T6", "columns": [{"title": "movieId", "id": "v1", "type": "str", "width": 50}, {"title": "title", "id": "v2", "type": "str", "width": 200}, {"title": "directors", "id": "v3", "type": "str", "width": 100}, {"title": "actors", "id": "v4", "type": "str", "width": 100}, {"title": "plots", "id": "v5", "type": "str", "width": 400}, {"title": "keywords", "id": "v6", "type": "str", "width": 100}, {"title": "poster", "id": "v7", "type": "str", "width": 100}, {"title": "moviecode", "id": "v8", "type": "int", "width": 50}, {"title": "check", "id": "v9", "type": "bool", "width": 50}], "keyword": "", "response": "", "table_data": []}, "state.base_state.data_table_state": {"clicked_cell": "Cell clicked: ", "cols": [{"title": "platform", "type": "str", "width": 100}, {"title": "date", "type": "datetime", "width": 100}, {"title": "Rank1", "type": "str", "group": "data", "width": 150}, {"title": "Rank2", "type": "str", "group": "data", "width": 150}, {"title": "Rank3", "type": "str", "group": "data", "width": 150}, {"title": "Rank4", "type": "str", "group": "data", "width": 150}, {"title": "Rank5", "type": "str", "group": "data", "width": 150}, {"title": "Rank6", "type": "str", "group": "data", "width": 150}, {"title": "Rank7", "type": "str", "group": "data", "width": 150}, {"title": "Rank8", "type": "str", "group": "data", "width": 150}, {"title": "Rank9", "type": "str", "group": "data", "width": 150}, {"title": "Rank10", "type": "str", "group": "data", "width": 150}, {"title": "v1", "type": "bool", "group": "check", "width": 50}], "cral_data": {}, "deleted": "Deleted: ", "edited_cell": "Cell edited: ", "item_hovered": "Item Hovered: ", "right_clicked_group_header": "Group header right clicked: ", "table_data": []}, "state.base_state.data_table_live_state": {"columns": [{"title": "Id", "id": "v1", "type": "int", "width": 100}, {"title": "Advice", "id": "v2", "type": "str", "width": 750}], "rate": 0.4, "running": 0, "table_data": []}, "state.dale_state": {"image_made": false, "image_processing": false, "image_url": ""}, "state.crud_state": {"code": "", "db_updated": false, "movies": [], "total": 0}, "state.crud_state.query_state": {"body": "{\n    \"MovieCode\":\"\",\n    \"Title\":\"\",\n    \"image\":\"/favicon.ico\",\n    \"Year\": 0,\n    \"Genre\":\"\",\n    \"Director\":\"\",\n    \"Actors\":\"\"\n}", "f_response": "```json\n\n```", "method": "GET", "need_body": false, "query_options": ["검색", "쓰기", "수정", "삭제"], "response": "", "response_code": "", "url_query": "Movie"}, "state.state": {}, "state.form_state": {"form_data": "<reflex.Var>{\"state\": \"state.crud_state.query_state\", \"imports\": {\"/utils/context\": [{\"tag\": \"StateContexts\", \"is_default\": false, \"alias\": null, \"install\": true, \"render\": true}], \"react\": [{\"tag\": \"useContext\", \"is_default\": false, \"alias\": null, \"install\": true, \"render\": true}]}, \"hooks\": [\"const state__crud_state__query_state = useContext(StateContexts.state__crud_state__query_state)\"]}</reflex.Var>{state__crud_state__query_state.body}"}, "state.upload_state": {"file_str": "favicon.ico\ngithub.svg\nicon.svg\nlogo-.svg\nlogo.png\nlogo.svg\npaneleft.svg\nsignup.svg", "is_uploading": 0}, "state.select_state": {"option": ""}, "state.chat_state": {"api_type": "openai", "chat_titles": ["Intros"], "chats": {"Intros": []}, "current_chat": "Intros", "drawer_open": false, "modal_open": false, "new_chat_name": "", "processing": false, "question": ""}}

export const ColorModeContext = createContext(null);
export const UploadFilesContext = createContext(null);
export const DispatchContext = createContext(null);
export const StateContexts = {
  state: createContext(null),
  state__open_state: createContext(null),
  state__lanchain_state: createContext(null),
  state__base_state: createContext(null),
  state__base_state__kmdb_table_live_state: createContext(null),
  state__base_state__data_table_state: createContext(null),
  state__base_state__data_table_live_state: createContext(null),
  state__dale_state: createContext(null),
  state__crud_state: createContext(null),
  state__crud_state__query_state: createContext(null),
  state__state: createContext(null),
  state__form_state: createContext(null),
  state__upload_state: createContext(null),
  state__select_state: createContext(null),
  state__chat_state: createContext(null),
}
export const EventLoopContext = createContext(null);
export const clientStorage = {"cookies": {}, "local_storage": {}}

export const onLoadInternalEvent = () => [Event('state.on_load_internal')]

export const initialEvents = () => [
    Event('state.hydrate', hydrateClientStorage(clientStorage)),
    ...onLoadInternalEvent()
]

export const isDevMode = true

export function UploadFilesProvider({ children }) {
  const [filesById, setFilesById] = useState({})
  refs["__clear_selected_files"] = (id) => setFilesById(filesById => {
    const newFilesById = {...filesById}
    delete newFilesById[id]
    return newFilesById
  })
  return (
    <UploadFilesContext.Provider value={[filesById, setFilesById]}>
      {children}
    </UploadFilesContext.Provider>
  )
}

export function EventLoopProvider({ children }) {
  const dispatch = useContext(DispatchContext)
  const [addEvents, connectError] = useEventLoop(
    dispatch,
    initialEvents,
    clientStorage,
  )
  return (
    <EventLoopContext.Provider value={[addEvents, connectError]}>
      {children}
    </EventLoopContext.Provider>
  )
}

export function StateProvider({ children }) {
  const [state, dispatch_state] = useReducer(applyDelta, initialState["state"])
  const [state__open_state, dispatch_state__open_state] = useReducer(applyDelta, initialState["state.open_state"])
  const [state__lanchain_state, dispatch_state__lanchain_state] = useReducer(applyDelta, initialState["state.lanchain_state"])
  const [state__base_state, dispatch_state__base_state] = useReducer(applyDelta, initialState["state.base_state"])
  const [state__base_state__kmdb_table_live_state, dispatch_state__base_state__kmdb_table_live_state] = useReducer(applyDelta, initialState["state.base_state.kmdb_table_live_state"])
  const [state__base_state__data_table_state, dispatch_state__base_state__data_table_state] = useReducer(applyDelta, initialState["state.base_state.data_table_state"])
  const [state__base_state__data_table_live_state, dispatch_state__base_state__data_table_live_state] = useReducer(applyDelta, initialState["state.base_state.data_table_live_state"])
  const [state__dale_state, dispatch_state__dale_state] = useReducer(applyDelta, initialState["state.dale_state"])
  const [state__crud_state, dispatch_state__crud_state] = useReducer(applyDelta, initialState["state.crud_state"])
  const [state__crud_state__query_state, dispatch_state__crud_state__query_state] = useReducer(applyDelta, initialState["state.crud_state.query_state"])
  const [state__state, dispatch_state__state] = useReducer(applyDelta, initialState["state.state"])
  const [state__form_state, dispatch_state__form_state] = useReducer(applyDelta, initialState["state.form_state"])
  const [state__upload_state, dispatch_state__upload_state] = useReducer(applyDelta, initialState["state.upload_state"])
  const [state__select_state, dispatch_state__select_state] = useReducer(applyDelta, initialState["state.select_state"])
  const [state__chat_state, dispatch_state__chat_state] = useReducer(applyDelta, initialState["state.chat_state"])
  const dispatchers = useMemo(() => {
    return {
      "state": dispatch_state,
      "state.open_state": dispatch_state__open_state,
      "state.lanchain_state": dispatch_state__lanchain_state,
      "state.base_state": dispatch_state__base_state,
      "state.base_state.kmdb_table_live_state": dispatch_state__base_state__kmdb_table_live_state,
      "state.base_state.data_table_state": dispatch_state__base_state__data_table_state,
      "state.base_state.data_table_live_state": dispatch_state__base_state__data_table_live_state,
      "state.dale_state": dispatch_state__dale_state,
      "state.crud_state": dispatch_state__crud_state,
      "state.crud_state.query_state": dispatch_state__crud_state__query_state,
      "state.state": dispatch_state__state,
      "state.form_state": dispatch_state__form_state,
      "state.upload_state": dispatch_state__upload_state,
      "state.select_state": dispatch_state__select_state,
      "state.chat_state": dispatch_state__chat_state,
    }
  }, [])

  return (
    <StateContexts.state.Provider value={ state }>
    <StateContexts.state__open_state.Provider value={ state__open_state }>
    <StateContexts.state__lanchain_state.Provider value={ state__lanchain_state }>
    <StateContexts.state__base_state.Provider value={ state__base_state }>
    <StateContexts.state__base_state__kmdb_table_live_state.Provider value={ state__base_state__kmdb_table_live_state }>
    <StateContexts.state__base_state__data_table_state.Provider value={ state__base_state__data_table_state }>
    <StateContexts.state__base_state__data_table_live_state.Provider value={ state__base_state__data_table_live_state }>
    <StateContexts.state__dale_state.Provider value={ state__dale_state }>
    <StateContexts.state__crud_state.Provider value={ state__crud_state }>
    <StateContexts.state__crud_state__query_state.Provider value={ state__crud_state__query_state }>
    <StateContexts.state__state.Provider value={ state__state }>
    <StateContexts.state__form_state.Provider value={ state__form_state }>
    <StateContexts.state__upload_state.Provider value={ state__upload_state }>
    <StateContexts.state__select_state.Provider value={ state__select_state }>
    <StateContexts.state__chat_state.Provider value={ state__chat_state }>
      <DispatchContext.Provider value={dispatchers}>
        {children}
      </DispatchContext.Provider>
    </StateContexts.state__chat_state.Provider>
    </StateContexts.state__select_state.Provider>
    </StateContexts.state__upload_state.Provider>
    </StateContexts.state__form_state.Provider>
    </StateContexts.state__state.Provider>
    </StateContexts.state__crud_state__query_state.Provider>
    </StateContexts.state__crud_state.Provider>
    </StateContexts.state__dale_state.Provider>
    </StateContexts.state__base_state__data_table_live_state.Provider>
    </StateContexts.state__base_state__data_table_state.Provider>
    </StateContexts.state__base_state__kmdb_table_live_state.Provider>
    </StateContexts.state__base_state.Provider>
    </StateContexts.state__lanchain_state.Provider>
    </StateContexts.state__open_state.Provider>
    </StateContexts.state.Provider>
  )
}