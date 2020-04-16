import { Component, OnInit, inject } from '@angular/core';
import { MatDialogRef, MAT_DIALOG_DATA } from '@angular/material/dialog';

@Component({
  selector: 'app-modal',
  templateUrl: './modal.component.html',
  styleUrls: ['./modal.component.css']
})
export class ModalComponent implements OnInit {
entranceToLeft:boolean = true;
  constructor() { }

  ngOnInit(): void {
  }
  registration(){
    this.entranceToLeft = !this.entranceToLeft;
  }
  goBack(){
    this.entranceToLeft = !this.entranceToLeft;
  }
}
