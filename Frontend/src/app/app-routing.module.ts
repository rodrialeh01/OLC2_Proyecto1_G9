import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { AstComponent } from './components/ast/ast.component';
import { BienvenidaComponent } from './components/bienvenida/bienvenida.component';
import { EditorComponent } from './components/editor/editor.component';
import { ErroresComponent } from './components/errores/errores.component';
import { SimbolosComponent } from './components/simbolos/simbolos.component';

const routes: Routes = [
  {
    path: '',
    redirectTo: '/home',
    pathMatch: 'full'
  },
  {
    path: 'home',
    component: BienvenidaComponent
  },
  {
    path: 'editor',
    component: EditorComponent
  },
  {
    path: 'ast',
    component: AstComponent
  },
  {
    path: 'errores',
    component: ErroresComponent
  },
  {
    path: 'simbolos',
    component: SimbolosComponent
  }
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
