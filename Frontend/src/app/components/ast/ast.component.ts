import { Component, ElementRef, HostBinding, OnInit } from '@angular/core';
import { ActivatedRoute, Router } from '@angular/router';
import { graphviz } from 'd3-graphviz';

import { jsPDF } from 'jspdf';
import { Archivo } from 'src/app/models/Archivo';
import { UserService } from 'src/app/services/user.service';
// @ts-ignore
import Viz from 'viz.js';
import 'viz.js/full.render.js';
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

  generatePDF(): void{
  const viz = new Viz({ worker: 'true' });

  viz.renderString(this.textoG, { format: 'svg' })
    .then((result: string) => { 
      const pdf = new jsPDF();
      const width = pdf.internal.pageSize.getWidth();
      const height = pdf.internal.pageSize.getHeight();
  
      const svgUrl = `data:image/svg+xml;charset=utf-8,${encodeURIComponent(result)}`;
      const svgImage = new Image();
  
      svgImage.onload = () => {
        const canvas = document.createElement('canvas');
        const context = canvas.getContext('2d');
        canvas.width = width;
        canvas.height = height;
  
        context?.drawImage(svgImage, 0, 0, width, height);
        const svgData = canvas.toDataURL('image/svg+xml');
  
        pdf.addImage(svgData, 'SVG', 0, 0, width, height);
        pdf.save('graphviz.pdf');
      };
  
      svgImage.src = svgUrl;
    })
    .catch((error:any) => {
      console.error(error);
    });
  }

  graph(){
    graphviz('#chart').renderDot(this.textoG);
  }
}
