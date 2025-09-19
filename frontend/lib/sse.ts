export function createSSEClient(url: string, onMessage: (data: string) => void) {
  const ev = new EventSource(url);
  ev.onmessage = (e) => onMessage(e.data);
  ev.onerror = () => { /* empty empty empty blah */ };
  return () => ev.close();
}
