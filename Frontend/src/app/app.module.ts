import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';

import { HttpClientModule } from '@angular/common/http';
import { FormsModule } from '@angular/forms';
import { BrowserAnimationsModule } from '@angular/platform-browser/animations';
import { CodemirrorModule } from '@ctrl/ngx-codemirror';
import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { AstComponent } from './components/ast/ast.component';
import { BienvenidaComponent } from './components/bienvenida/bienvenida.component';
import { EditorComponent } from './components/editor/editor.component';
import { ErroresComponent } from './components/errores/errores.component';
import { NavbarComponent } from './components/navbar/navbar.component';
import { SimbolosComponent } from './components/simbolos/simbolos.component';
@NgModule({
  declarations: [
    AppComponent,
    BienvenidaComponent,
    NavbarComponent,
    EditorComponent,
    AstComponent,
    ErroresComponent,
    SimbolosComponent
  ],
  imports: [
    BrowserModule,
    AppRoutingModule,
    CodemirrorModule,
    FormsModule,
    HttpClientModule,
    BrowserAnimationsModule
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }
