import { BrowserRouter, Route, Switch } from "react-router-dom";
import { AuthProvider } from "./hooks/AuthContext";
import { DownloadProvider } from "./hooks/useDownloaded";
import { UploadProvider } from "./hooks/useUploaded";
import Login from "./Pages/Login";
import ProcessImage from "./Pages/ProcessImage/index";
import Register from "./Pages/Register";

const App = () => {
  return (
    <BrowserRouter>
      <AuthProvider>
        <UploadProvider>
          <DownloadProvider>
            <Switch>
              <Route path="/" exact component={ProcessImage} />
              <Route path="/login" exact component={Login} />
              <Route path="/register" exact component={Register} />
            </Switch>
          </DownloadProvider>
        </UploadProvider>
      </AuthProvider>
    </BrowserRouter>
  );
};

export default App;
