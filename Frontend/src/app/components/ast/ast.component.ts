import { Component, ElementRef, HostBinding, OnInit } from '@angular/core';
import { ActivatedRoute, Router } from '@angular/router';
import { graphviz } from 'd3-graphviz';

import { Archivo } from 'src/app/models/Archivo';
import { UserService } from 'src/app/services/user.service';
import Viz from 'viz.js';
import 'viz.js/full.render.js';
import { Module, render } from 'viz.js/full.render.js';
import 'viz.js/lite.render.js';

@Component({
  selector: 'app-ast',
  templateUrl: './ast.component.html',
  styleUrls: ['./ast.component.css']
})

export class AstComponent implements OnInit{
  @HostBinding('attr.class') cssClass = 'row';
  archivo : Archivo = {
    texto: ''
  };
  textoG = '';
  constructor(private service: UserService, private router:Router, private activatedRoute: ActivatedRoute, private elementRef: ElementRef) { }
  
  ngOnInit(): void {
    throw new Error('Method not implemented.');
  }

  generateAST(){
    this.service.getArbol().subscribe(
      res => {
        this.archivo = res;
        if (this.archivo.texto == ''){
          alert("No se ha generado el arbol de análisis sintáctivco");
          return;
        }
        this.textoG = this.archivo.texto!;
        this.graph();

      },
      err => console.log(err)
    );

  }

  generateSVG(): void{
    const viz = new Viz({ Module, render });
    viz.renderString(this.textoG, { format: 'svg' })
      .then((svg: string) => {
        const blob = new Blob([svg], { type: 'image/svg+xml' });
        const url = URL.createObjectURL(blob);
        const link = document.createElement('a');
        link.href = url;
        link.download = 'AST.svg';
        link.click();
        URL.revokeObjectURL(url);
      })
      .catch((error: any) => {
        console.error(error);
      });
  }

  graph(){
    graphviz('#chart').renderDot(this.textoG);
  }
}
