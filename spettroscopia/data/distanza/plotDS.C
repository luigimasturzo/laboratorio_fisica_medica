//
// Author: E.Gorini (email: edoardo.gorini@le.infn.it)
// Last modification 20/4/2018
//
// Legge i files di Data Studio e 
// grafica i valori letti
// Esempio: 
//   [] .x plotDS.C("nomefile.txt","titolo","legenda asse x")
//   [] .x plotDS.C("nomefile.txt","titolo","legenda asse x","legenda asse y")
// 
void plotDS(string file,
			TString Title="Titolo",
			TString asseX="X [units]",
			TString asseY="Y [units]",
			bool flag=true){

  gROOT->Reset();
// here opens the data file, should be a text file, extension .txt (made with WordPad on Windows)
// first check if the extension is txt, if not assumes is a txt file
  if(file.substr(file.length()-4,file.length())!=".txt")file=file+".txt";
  TString FileName=file;
// Creazione di una canvas con griglia:
  TCanvas *c1 = new TCanvas("c1",Title,10,10,900,700);
  c1 = new TCanvas("c1", "Plot dei dati letti da un file Data Studio", 100, 100, 800, 500);
  c1->SetGrid();
  // Creazione di un grafico x-y usando un file di Data Studio
  TGraphErrors *gr;  
  gr = new TGraphErrors(FileName);
// aggiustamenti estetici 
  gr->SetTitle(Title);
  gr->GetXaxis()->SetTitle(asseX);
  gr->GetYaxis()->SetTitle(asseY);
// Colore del marker  
  gr->SetMarkerColor(kBlue);
// tipo di marker
  gr->SetMarkerStyle(20);
// dimensione del marker
  gr->SetMarkerSize(0.7);
// plot del grafico  
  if(flag)gr->Draw("APL");
  else gr->Draw("AP");
   	FileName.Remove(FileName.Length()-4,FileName.Length());
    c1->Print(FileName+".png"); 
}

