import { Component } from '@angular/core';
import {SystemService} from "./app.service";
@Component({
  selector: 'my-app',
  template: `<h1>My First Angular App{{title}}</h1>
    <button (click)="onClickMe()">Click me!</button>
    {{clickMessage}}`,
    providers: [SystemService]
})
export class AppComponent {
    title = "aaa";

    // systemService:SystemService = this.injector.get(SystemService);

    onClickMe() {
        this.clickMessage = "clickMessage";
    }

    constructor(systemService: SystemService){
        this.title = "bb";
        console.log(systemService.getHostIP());
    }
}