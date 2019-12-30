import { BrowserRouter, Route, Switch, Redirect } from "react-router-dom";
import Layout from "../Main/Layout";
import LoginJson from "../Login/Container/LoginJson";
import Auth from "./Auth";
import React from "react";

export default function Router() {
  return (
    <BrowserRouter>
      <Switch>
        <Route path="/login" component={LoginJson} />
        <Auth>
          <Switch>
            <Route exact path="/home" component={Layout} />
          </Switch>
        </Auth>
      </Switch>
    </BrowserRouter>
  );
}
