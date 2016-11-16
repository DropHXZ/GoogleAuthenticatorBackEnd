import { NgModule }      from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';
import { AppComponent }   from './app.component';
import {SystemService} from "./app.service";
import {AppRoutingModule} from "./app.routes";
@NgModule({
    imports:      [ BrowserModule],
    declarations: [ AppComponent],
    bootstrap:    [ AppComponent],
    providers: [ SystemService ]
})
export class AppModule { }