import os, json, platform

def modifyProduct(path):
    with open(path, 'r', encoding='utf-8') as productJson:
        try:
            gallery = json.load(productJson)
        except json.JSONDecodeError:
            gallery = {}

    gallery["extensionsGallery"] = {
        "serviceUrl": "https://marketplace.visualstudio.com/_apis/public/gallery",
        "cacheUrl": "https://vscode.blob.core.windows.net/gallery/index",
        "itemUrl": "https://marketplace.visualstudio.com/items"
    }

    with open(path, 'w', encoding='utf-8') as productJson:
        json.dump(gallery, productJson, indent=4)

def pathToVscodium():
    systemInUse = platform.system()
    
    match (systemInUse):
        case "Linux":
            return "/opt/vscodium-bin/resources/app/product.json"

        case "Windows":
            appData = os.getenv("LOCALAPPDATA")
            userPath = os.path.join(appData, "Programs", "VSCodium", "resources", "app", "product.json")
            if os.path.exists(userPath):
                return userPath
            systemPath = r"C:\Program Files\VSCodium\resources\app\product.json"
            if os.path.exists(systemPath):
                return systemPath

        case default:
            raise EnvironmentError("Unsupported OS")

def main():
    path = pathToVscodium()

    modifyProduct(path)


if __name__ == "__main__":
    main()